from flask import Flask
import socket

from src.controllers.contabilidad_controller import ContabilidadController

app = Flask(__name__)

contabilidad_controller = ContabilidadController()

# Define routes here using contabilidad_controller

if __name__ == '__main__':
    app.run(host=socket.gethostbyname(socket.gethostname()), port=8000)