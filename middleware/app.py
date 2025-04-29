from flask import Flask
import socket

from src.controllers.middleware_controller import MiddlewareController

app = Flask(__name__)

midd_cotroller = MiddlewareController()

@app.route('/clientes', methods=['POST'])
def clientes():
    """
    Maneja las peticiones relacionadas con los clientes.
    """
    return midd_cotroller.clientes()


if __name__ == '__main__':
    app.run(debug=True,host= socket.gethostbyname(socket.gethostname()),port=8000) 