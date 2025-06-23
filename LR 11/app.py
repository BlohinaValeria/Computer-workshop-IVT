from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- Добавьте эту строку
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

app = Flask(__name__)
CORS(app)


@app.route("/login", methods=["GET"])
def login():
    return jsonify({"author": "1147331"})

@app.route("/decypher", methods=["POST"])
def decypher():
    if "key" not in request.files or "secret" not in request.files:
        return jsonify({"error": "Требуется файл ключа и зашифрованного сообщения"}), 400

    key_file = request.files["key"]
    secret_file = request.files["secret"]

    try:
        private_key = RSA.import_key(key_file.read())
        cipher = PKCS1_OAEP.new(private_key)
        encrypted_data = base64.b64decode(secret_file.read())
        decrypted_data = cipher.decrypt(encrypted_data)
        return decrypted_data.decode("utf-8")
    except Exception as e:
        return jsonify({"error": f"Ошибка при расшифровке: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)