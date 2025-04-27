from flask import Flask
import socket

from src.controllers.compras_ventas_controller import ComprasVentasController

app = Flask(__name__)

compras_ventas_controller = ComprasVentasController()

# Define routes here using compras_ventas_controller

if __name__ == '__main__':
    app.run(host=socket.gethostbyname(socket.gethostname()), port=8000)