from flask import Flask
import socket

from src.controllers.atencion_proveedor_controller import AtencionProveedorController
app = Flask(__name__)

atencion_proveedor_controller = AtencionProveedorController()

# Define routes here using atencion_proveedor_controller

if __name__ == '__main__':
    app.run(host=socket.gethostbyname(socket.gethostname()), port=8000)