from flask import Flask
import socket

from src.controllers.middleware_controller import MiddlewareController

app = Flask(__name__)

midd_cotroller = MiddlewareController()

app.add_url_rule('/clientes',view_func=midd_cotroller.clientes, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True,host= socket.gethostbyname(socket.gethostname()),port=8000) 