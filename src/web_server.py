# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import os

par_dir = os.path.abspath(os.path.join(__file__, os.pardir))
par_dir = os.path.abspath(os.path.join(par_dir, os.pardir))
templates_dir = os.path.join(par_dir, "templates")


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def do_GET(self) -> None:
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        path = self.path
        if path.startswith('/'):
            if path == '/':
                path = 'main'
            else:
                path = path[1:]
        filename = os.path.join(templates_dir, f'{path}.html')
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        self.wfile.write(content.encode())  # Тело ответа

    def _set_response(self):
        """ Отправление заголовков ответа сервера, что все хорошо"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

    def do_POST(self) -> None:
        """ Метод для обработки входящих POST-запросов """
        content_type = self.headers.get('content-type')
        content_length = int(self.headers['Content-Length'])

        # if content_type == 'multipart/form-data':
        #     postvars = parse_multipart(self.rfile, pdict)
        if content_type == 'application/x-www-form-urlencoded':
            postvars = parse_qs(self.rfile.read(content_length).decode('utf-8'))
        else:
            postvars = {}

        self._set_response()

        username = postvars.get('send_from')
        email = postvars.get('email')
        mail_message = postvars.get('message')
        if username and email and mail_message:
            if isinstance(username, list):
                username = username[0]
            if isinstance(email, list):
                email = email[0]
            if isinstance(mail_message, list):
                mail_message = mail_message[0]

            message = (u"<body><h3>Пользователь {} на почту {} отправил сообщение '{}'</h3></body>").format(username,
                                                                                                            email,
                                                                                                            mail_message)
            self.wfile.write(message.encode('utf-8'))
