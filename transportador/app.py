from flask import Flask
import socket

from src.controllers.transportador_controller import TransportadorController

app = Flask(__name__)

transportador_controller = TransportadorController()

@app.route('/ordenar_transporte', methods=['POST'])
def ordenar_transporte():
    """
    Endpoint para ordenar el transporte de productos.

    Este endpoint recibe una solicitud para ordenar el transporte de productos y llama al controlador correspondiente.

    Returns:
        dict: Un diccionario con la respuesta a la solicitud.
    """
    return transportador_controller.ordenar_transporte()

if __name__ == '__main__':
    app.run(debug=True,host=socket.gethostbyname(socket.gethostname()), port=8000)