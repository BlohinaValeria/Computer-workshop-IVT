# Лабораторная работа 6

## Задание 
Напишите корневой адрес работающего по https веб-приложения (+ ссылку на борд/репозиторий с кодом решения), которое по маршруту /size2json получает по имени поля image в формате multipart/form-data изображение в формате PNG и выдаёт JSON-строку вида {"width":123,"height":456}, содержащую, соответственно, ширину и высоту изображения в пикселях.

По маршруту /login приложение должно выдавать ваш логин в этой системе (MOODLE).

_Требования:_ 

+ Все данные возвращаются в json, заголовки ответов должны быть соответствующие данным.
+ Формат ответа по маршруту /login {"author": "__ваш логин__"}
+ Если передана не картинка, возвращать json: {"result":"invalid filetype"}

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
[скриншот](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%206/replit.png)

# POST запрос в Insomnia
[пост запрос](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%206/test.png)
  

