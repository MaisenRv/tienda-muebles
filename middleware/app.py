from flask import Flask
import socket
from flasgger import Swagger, swag_from

from src.controllers.middleware_controller import MiddlewareController

app = Flask(__name__)

swagger = Swagger(app, template = {
    "swagger": "2.0",
    "info": {
        "title": "Middleware API",
        "description": "API para manejar las peticiones relacionadas con los clientes y proveedores.",
        "version": "1.0.0"
    }
})

midd_cotroller = MiddlewareController()

@app.route('/clientes', methods=['POST'])
@swag_from('src/docs/clientes.yml')
def clientes():
    return midd_cotroller.clientes()

@app.route('/proveedores', methods=['POST'])
@swag_from('src/docs/proveedores.yml')
def proveedores():
    return midd_cotroller.proveedores()     
           
if __name__ == '__main__':
    app.run(debug=True,host= socket.gethostbyname(socket.gethostname()),port=8000) 