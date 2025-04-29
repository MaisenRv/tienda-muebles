from flask import Flask
import socket

from src.controllers.tienda_controller import TiendaController

app = Flask(__name__)

tienda_controller = TiendaController()

app.add_url_rule('/tienda/atenderCliente', view_func=tienda_controller.atender_cliente, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True,host=socket.gethostbyname(socket.gethostname()), port=8000)