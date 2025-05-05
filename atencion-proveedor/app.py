from flask import Flask
import socket
from flasgger import Swagger, swag_from


from src.controllers.atencion_proveedor_controller import AtencionProveedorController
app = Flask(__name__)
swagger = Swagger(app, template = {
    "swagger": "2.0",
    "info": {
        "title": "Atencion Proveedor API",
        "description": "API para manejar las peticiones relacionadas con los proveedores.",
        "version": "1.0.0"
    }
})

atencion_proveedor_controller = AtencionProveedorController()

@app.route('/atencion-proveedor/atenderProveedor', methods=['POST'])
@swag_from('src/docs/atender_proveedor.yml')
def atender_proveedor():
    return atencion_proveedor_controller.atender_proveedor()

if __name__ == '__main__':
    app.run(debug=True,host=socket.gethostbyname(socket.gethostname()), port=8000)