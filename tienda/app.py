from flask import Flask
import socket
from flasgger import Swagger, swag_from

from src.controllers.tienda_controller import TiendaController


app = Flask(__name__)
swagger = Swagger(app, template= {
    "swagger": "2.0",
    "info": {
        "title": "API Tienda",
        "description": "Documentación automática con Swagger",
        "version": "1.0.0"
    }
})

tienda_controller = TiendaController()

@app.route('/tienda/atenderCliente', methods=['POST'])
@swag_from('src/docs/atender_cliente.yml')
def atender_cliente():
    return tienda_controller.atender_cliente()


if __name__ == '__main__':
    app.run(debug=True,host=socket.gethostbyname(socket.gethostname()), port=8000)