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
def cargar_productos():
    """
    Carga los productos disponibles en el inventario.
    ---
    tags:
      - Inventario
    responses:
      200:
        description: Lista de productos en inventario.
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              nombre:
                type: string
              precio_unitario:
                type: number
              cantidad_disponible:
                type: integer
    """
    return inventario_controller.cargar_productos()

@app.route('/inventario/cargarRequerimientosProductos', methods=['GET'])
@swag_from('src/docs/cargar_requerimientos_productos.yml')
def cargar_requerimientos_productos():
    return inventario_controller.cargar_requerimientos_productos()


@app.route('/inventario/validarProductos', methods=['POST'])
def validar_productos():
    """
    Valida la existencia y cantidad de productos en el inventario.
    ---
    tags:
      - Inventario
    parameters:
      - name: productos
        in: body
        required: true
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              cantidad:
                type: integer
    responses:
      200:
        description: Productos validados correctamente.
        schema:
          type: object
          properties:
            productos_validos:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  nombre:
                    type: string
                  precio_unitario:
                    type: number
                  cantidad:
                    type: integer
      400:
        description: Error en la validación de productos.
        schema:
          type: object
          properties:
            error:
              type: string
    """
    return inventario_controller.validar_productos()

if __name__ == '__main__':
    app.run(debug=True,host=socket.gethostbyname(socket.gethostname()), port=8000)