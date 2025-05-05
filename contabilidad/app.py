from flask import Flask
import socket
from flasgger import Swagger, swag_from

from src.controllers.contabilidad_controller import ContabilidadController

app = Flask(__name__)
swagger = Swagger(app, template= {
    "swagger": "2.0",
    "info": {
        "title": "API Contabilidad",
        "description": "Documentación automática con Swagger",
        "version": "1.0.0"
    }
})

contabilidad_controller = ContabilidadController()

@app.route('/contabilidad/generarFactura', methods=['POST'])
@swag_from("src/docs/generar_factura.yml")
def generar_factura():
    return contabilidad_controller.generar_factura()

@app.route('/contabilidad/recibirFactura', methods=['POST'])
@swag_from("src/docs/recibir_factura.yml")
def recibir_factura():
    return contabilidad_controller.recibir_factura()


if __name__ == '__main__':
    app.run(debug=True,host=socket.gethostbyname(socket.gethostname()), port=8000)