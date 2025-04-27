from flask import Flask
import socket

from src.controllers.tienda_controller import TiendaController

app = Flask(__name__)

tienda_controller = TiendaController()

# Define routes here using tienda_controller

if __name__ == '__main__':
    app.run(host=socket.gethostbyname(socket.gethostname()), port=8000)