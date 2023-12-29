import os

import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv

#mis propias librerias
from lib.allowed_user import is_user_allowed

#Cargar configuraciones basicas
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Carga las variables de entorno del archivo .env
load_dotenv()
TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

# Almacena el historial de mensajes para cada usuario
message_history = {}

def error_handler(update: Update, context: CallbackContext) -> None:
    logging.error(f'Error en la actualización {update} causado por {context.error}')

#esto es un decorador
def message_type_middleware(func):
    def inner(update: Update, context: CallbackContext):
        message_type = None
        if update.message.voice:
            message_type = 'voice'
        elif update.message.photo:
            message_type = 'photo'
        elif update.message.text:
            message_type = 'text'
        else:
            return

        return func(update, context, message_type)

    return inner

#esta es la opcion de ayuda /help
def help (update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if not is_user_allowed(update):
        update.message.reply_text("Solicita acceso a @cejebuto con tu ID de usuario de Telegram : " + str(user_id))
        return
    update.message.reply_text("Este bot se usa para ... ")
    update.message.reply_text("Puedes enviar una imagen o foto y el bot ... ")

#esta es la opcion de bienvenida /start
def start(update: Update , context: CallbackContext):
    if not is_user_allowed(update):
        update.message.reply_text("Lo siento, este bot es privado y solo está disponible para usuarios autorizados.")
        update.message.reply_text("/help para ayuda")
        return
    update.message.reply_text('¡Hola! Envía un mensaje ... ')

#Este es el controlador , recibe voz, imgen o texto
@message_type_middleware
def chat_response(update: Update, context: CallbackContext,message_type):

    switch_cases = {
        'voice': handle_voice,
        'photo': handle_photo,
        'text': handle_text
    }
    switch_cases.get(message_type, lambda u, c: None)(update, context)

#FUNCIONES DE CONTROLADORES PRINCIPALES
#Texto
def handle_text(update: Update, context: CallbackContext):
    #Procesamos el texto del mensaje, recordar llamrlo con update y context
    input_text = update.message.text
    #request_by_text(input_text, message_history, update, context)

#Voz
def handle_voice(update: Update, context: CallbackContext):

    # Envía el mensaje "Escuchando..." y guarda el objeto del mensaje en una variable
    update.message.reply_text("Funcion no implementada")


def handle_photo(update: Update, context: CallbackContext):

    # Obtén la imagen del mensaje
    # photo_file = context.bot.get_file(update.message.photo[-1].file_id)

    update.message.reply_text("Funcion no implementada")


#MAIN
def main():
    updater = Updater(TELEGRAM_API_TOKEN)

    dp = updater.dispatcher
    dp.add_error_handler(error_handler)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler((Filters.text | Filters.voice | Filters.photo) & ~Filters.command, chat_response))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
