# Импорт встроенной библиотеки для работы веб-сервера
from http.server import BaseHTTPRequestHandler, HTTPServer
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
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа
        filename = os.path.join(templates_dir, 'contacts.html')
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        self.wfile.write(content.encode()) # Тело ответа

