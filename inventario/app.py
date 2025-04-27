from flask import Flask
import socket

from src.controllers.inventario_controller import InventarioController

app = Flask(__name__)

inventario_controller = InventarioController()

# Define routes here using inventario_controller

if __name__ == '__main__':
    app.run(host=socket.gethostbyname(socket.gethostname()), port=8000)