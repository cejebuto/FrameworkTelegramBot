# Framework para Bot de telegram.

Este repositorio contiene el código fuente para un Frameworkd para un bot de Telegram.

## Requisitos

Debe tener una cuenta de Telegram y un bot de Telegram configurado. Puede encontrar instrucciones para crear un bot de Telegram en [este enlace](https://core.telegram.org/bots#6-botfather).


## Configuración

1. Copie `.env.example` a un nuevo archivo llamado `.env`.
2. Complete las variables de entorno en el archivo `.env`:

```
TELEGRAM_API_TOKEN=<your_telegram_api_token>
```

3. Copie `allowed_user_ids.json.example` a `allowed_user_ids.json` y separe por comas los id's de telegram que desee permitir que usen el bot:
```
[
    <your_telegram_user_id>,
    <your_telegram_user_id>,
]
```
- Puede encontrar su id de telegram en @userinfobot


## Construcción de la imagen Docker

1. Construye la imagen de Docker:

```sh
docker build -t mybot .
```

## Ejecución

### Linux / macOS / Windows

```bash
docker run --rm -it --env-file .env mybot
```

## Desarrollo

### con hupper (actualización en caliente)

#### Linux / macOS 

```bash
docker run --rm -it --env-file .env -v $(pwd):/app -e RUN_MODE=hupper mybot
```

#### Windows

```bash
docker run --rm -it --env-file .env -v ${PWD}:/app -e RUN_MODE=hupper mybot
```


## Uso en Telegram

**Uso común**

- `El uso depende lo que se requiera el bot`



---


## Licencia
GNU General Public License v3.0