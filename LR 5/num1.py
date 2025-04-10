import socketserver
import datetime
import locale

MOODLE_LOGIN = "1147331"
try:
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, 'ru_RU')
    except locale.Error:
        print("Warning: Unable to set locale. Using default.")


class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        now = datetime.datetime.now()
        formatted_date_time = now.strftime("%d.%m.%y %H:%M:%S")

        response_text = f"{MOODLE_LOGIN}, {formatted_date_time}\n"
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain; charset=utf-8\r\n"
            f"Content-Length: {len(response_text)}\r\n"
            "\r\n"
            f"{response_text}"
        ).encode('utf-8')

        self.request.sendall(response)


if __name__ == "__main__":
    HOST, PORT = "localhost", 8000

    with socketserver.TCPServer((HOST, PORT), MyHandler) as server:
        print(f"Server started at http://{HOST}:{PORT}/")
        server.serve_forever()