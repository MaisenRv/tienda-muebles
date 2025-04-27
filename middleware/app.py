from flask import Flask
import socket

from src.controllers.middleware_controller import MiddlewareController

app = Flask(__name__)

midd_cotroller = MiddlewareController()

app.add_url_rule('/hola',view_func=midd_cotroller.hello, methods=['POST'])

if __name__ == '__main__':
    app.run(host= socket.gethostbyname(socket.gethostname()),port=8000) 