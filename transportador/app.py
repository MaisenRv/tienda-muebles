from flask import Flask
import socket

from src.controllers.transportador_controller import TransportadorController

app = Flask(__name__)

transportador_controller = TransportadorController()

# Define routes here using transportador_controller

if __name__ == '__main__':
    app.run(host=socket.gethostbyname(socket.gethostname()), port=8000)