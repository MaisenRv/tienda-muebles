from flask import Flask
import socket
from flasgger import Swagger, swag_from

from src.controllers.transportador_controller import TransportadorController

app = Flask(__name__)
swager = Swagger(app, template= {
    "swagger": "2.0",
    "info": {
        "title": "API Transportador",
        "description": "Documentación automática con Swagger",
        "version": "1.0.0"
    }
})

transportador_controller = TransportadorController()

@app.route('/transportador/ordenarTransporte', methods=['POST'])
@swag_from('src/docs/ordenar_transporte.yml')
    
def ordenar_transporte():
    return transportador_controller.ordenar_transporte()

if __name__ == '__main__':
    app.run(debug=True,host=socket.gethostbyname(socket.gethostname()), port=8000)