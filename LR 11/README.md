# Лабораторная работа по теме №11 Ассиметричное шифрование 

## Задание 
Напишите корневой адрес работающего по https веб-приложения и ссылку на гитхаб-репозиторий с кодом и отчетом-демонстрацией работы приложения, которое по маршруту /decypher получает в формате multipart/form-data приватный ключ для расшифровки (имя поля формы key) и зашифрованное содержимое (имя поля формы secret) и выдаёт в виде обычной строки результат расшифровки.

Требования к решению: 
:small_red_triangle:  Фреймворк Flask или FastAPI или любой другой Python-framework (микро-фреймворк - без развесистой структуры файлов и папок внутри). 
:small_red_triangle:  Формат ответа по маршруту /login {"author": "__ваш логин__"}
:small_red_triangle:  Реализация дополнительных решений более чем с 1 фреймворком (варианты: Node.js, Django, Go). 
:small_red_triangle:  Реализация фронтэнда и отправка данных на сервер с использованием какого-либо фронтэнд-фреймворка или библиотеки (Vue.js, Svelte, React).
:small_red_triangle:  Вывод и отображение исходного текста на страницу с формой (без перезагрузки страницы, асинхронно).

# Код программы без усложнения
  ```python
from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS  
from PIL import Image, ImageDraw
import io
import base64
import os

app = Flask(__name__)
CORS(app)  

@app.route('/')
def home():
    return "Flask Image Generator is Running!"

@app.route('/login', methods=['GET'])
def login():
    return jsonify({"author": "1147331"})

@app.route('/makeimage', methods=['GET', 'POST'])
def make_image():
    if request.method == 'GET':
        return render_template('makeimage.html')

    try:
        width = int(request.form.get('width'))
        height = int(request.form.get('height'))
        text = request.form.get('text', '')

        if width <= 0 or height <= 0:
            return render_template('makeimage.html', message="Invalid image size")

        img = Image.new('RGB', (width, height), color=(73, 109, 137))
        d = ImageDraw.Draw(img)
        d.text((10, 10), text, fill=(255, 255, 0))

        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        img_byte_arr.seek(0)

        return send_file(img_byte_arr, mimetype='image/jpeg')


    except (ValueError, TypeError):
        return render_template('makeimage.html', message="Invalid image size")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Убираем ssl_context для Replit
  ```
# Реализация шаблона 
![скриншот](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%2010/replit.png)

# Сгенерированное изображение 
![скриншот](https://github.com/BlohinaValeria/Computer-workshop-IVT/blob/main/LR%2010/generate.png)
