## Задание:
Создайте бота-переводчика для Telegram с использованием Cloud Functions и API Gateway.
Вы можете выбрать любые язык программирования (из поддерживаемых Yandex Cloud) и библиотеку для взаимодействия с Telegram Bot API.
Бот должен обрабатывать команды `/start` и `/help`. Любой другой ввод должен обрабатываться ботом как текст, который необходимо перевести на другой язык (любой на выбор студента).
Для перевода используйте LibreTranslate (сайт, репозиторий). Публичный сервер, для использования которого не нужен API-ключ: https://translate.flossboxin.org.in/ (см. раздел Mirrors на странице GitHub).

## В ответе необходимо указать:

:triangular_flag_on_post: адрес Cloud Function и скриншот кода функции:
https://functions.yandexcloud.net/d4ermk9vp1q3jt0pi37n

![](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%207/cloud.png)

    ```
    import json
    import requests
    import telebot
    import os

    BOT_TOKEN = os.environ.get('TOKEN_BOT')

    if not BOT_TOKEN:
        raise ValueError("Telegram bot token not provided in the environment variables.")

    bot = telebot.TeleBot(BOT_TOKEN)

    # URL LibreTranslate
    LIBRETRANSLATE_URL = "https://translate.flossboxin.org.in/translate"
    TARGET_LANGUAGE = "en"

    def translate_text(text, target_language):
        """Переводит текст на указанный язык."""
        try:
            response = requests.post(
                LIBRETRANSLATE_URL,
                json={
                    "q": text,
                    "source": "auto",
                    "target": target_language,
                    "format": "text"
                }
            )
            response.raise_for_status()
            return response.json()["translatedText"]
        except requests.exceptions.RequestException as e:
            return f"Ошибка перевода: {e}"

    @bot.message_handler(commands=['start', 'help'])
    def handle_start_help(message):
        """Обрабатывает команды /start и /help."""
        if message.text == "/start":
            bot.reply_to(message, "Здравствуй! Я бот-переводчик. Отправь мне текст, и я переведу его на английский.")
        elif message.text == "/help":
            bot.reply_to(message, "Я перевожу любой текст на английский язык. Используйте команду /start для начала работы.")

    @bot.message_handler(func=lambda message: True)
    def translate_message(message):
        """Переводит текст."""
        translated_text = translate_text(message.text, TARGET_LANGUAGE)
        bot.reply_to(message, translated_text)

    def handler(event, context):
        """Обработчик Cloud Functions."""
        try:
            bot.process_new_messages([telebot.types.Update.de_json(event['body']).message])
            return {
                'statusCode': 200,
                'body': 'OK'
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': f'Error: {str(e)}'
            }
    ```

:triangular_flag_on_post: описание API Gateway и скриншот:

    ![](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%207/api.png)
    
    Спецификация

    ```yaml
    openapi: 3.0.0
    info:
      title: Sample API
      version: 1.0.0
    servers:
      - url: https://d5dn5fe519oia6gu5ugm.pdkwbi1w.apigw.yandexcloud.net
    paths:
      /:
        post:
          x-yc-apigateway-integration:
            type: cloud_functions
            function_id: d4ermk9vp1q3jt0pi37n
          operationId: tgbot
    ```
  :triangular_flag_on_post:  ник Telegram-бота.
    @translatecomppr_bot
