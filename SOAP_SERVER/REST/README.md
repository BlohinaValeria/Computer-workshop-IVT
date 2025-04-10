# Тема 4 Основы работы с SoapUI - REST сервисы

## Задание 
Создайте проект с применением открытых публичных REST сервисов. Придумайте любой бизнес-процесс на их основе (последовательность действий) и реализуйте его тестирование в SoapUI - создайте TestCase.

# Проект: Проверка факта о кошках (Cat Facts Service)

:heavy_exclamation_mark: _Последовательность действий_

1. Отправка запроса: Отправляем GET запрос к Cat Facts Service.
2. Получение ответа: Получаем JSON-ответ, содержащий случайный факт о кошках.
3. Проверка структуры ответа: проверяем, содержит ли ответ поле «факт».
4. Проверка факта (содержит слово “cat”): проверяем, что поле “fact” содержит слово “cat” (или любую другую подстроку).

:heavy_exclamation_mark: Используемые сервисы:
- [ ] _Cat Facts Service:_ бесплатный публичный REST-сервис, возвращающий случайный факт о кошках.
- [ ] URL -адрес: https://catfact.ninja/fact


+ Создание проекта в SoapUI: 
![создание](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/SOAP_SERVER/REST/название%20и%20создание.png)

+ Создайте Resource:
![resource](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/SOAP_SERVER/REST/url.png)

+ 
# Код программы
  ```python
from flask import Flask, request, jsonify
from PIL import Image
import io

app = Flask(__name__)

MY_LOGIN = "1147331" 

@app.route("/size2json", methods=['POST'])
def size2json():
    if 'image' not in request.files:
        return jsonify({"result": "no file part"}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({"result": "no selected file"}), 400

    try:
        img = Image.open(io.BytesIO(image_file.read()))
        width, height = img.size
        return jsonify({"width": width, "height": height}), 200
    except Exception as e:
        print(e)
        return jsonify({"result": "invalid filetype"}), 400


@app.route("/login")
def login():
    return jsonify({"author": MY_LOGIN}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
  ```
# Борд в Replit
![скриншот](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%206/replit.png)

# POST запрос в Insomnia
![пост запрос](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%206/test.png)
  
# Ссылка 
https://e15b1ecc-cea0-469e-9d46-3a70a6f66586-00-2jiuziqs4l4at.pike.replit.dev/login
