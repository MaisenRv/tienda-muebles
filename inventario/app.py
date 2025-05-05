from flask import Flask
import socket
from flasgger import Swagger, swag_from

from src.controllers.inventario_controller import InventarioController

app = Flask(__name__)
swagger = Swagger(app, template={
     
    "info": {
        "title": "API de Inventario",
        "version": "1.0.0",
        "description": "API para gestionar el inventario de productos."
    }
})

inventario_controller = InventarioController()

@app.route('/inventario/actualizarInventario', methods=['POST'])
@swag_from('src/docs/actualizar_inventario.yml')
def actualizar_inventario():
  return inventario_controller.actualizar_inventario()

@app.route('/inventario/cargarProductos', methods=['GET'])
@swag_from('src/docs/cargar_productos.yml')
def cargar_productos():
    return inventario_controller.cargar_productos()

@app.route('/inventario/cargarRequerimientosProductos', methods=['GET'])
@swag_from('src/docs/cargar_requerimientos_productos.yml')
def cargar_requerimientos_productos():
    return inventario_controller.cargar_requerimientos_productos()


@app.route('/inventario/validarProductos', methods=['POST'])
@swag_from('src/docs/validar_productos.yml')
def validar_productos():
    return inventario_controller.validar_productos()

if __name__ == '__main__':
    app.run(debug=True,host=socket.gethostbyname(socket.gethostname()), port=8000)