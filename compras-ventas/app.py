from flask import Flask
import socket
from flasgger import Swagger

from src.controllers.compras_ventas_controller import ComprasVentasController

app = Flask(__name__)
swagger = Swagger(app, template={
    "swagger": "2.0",
    "info": {
        "title": "Compras y Ventas API",
        "version": "1.0.0"
    }
})

compras_ventas_controller = ComprasVentasController()

@app.route('/compras-ventas/registrarCompra', methods=['POST'])
def registrar_compra():
    return compras_ventas_controller.registrar_compra()

@app.route('/compras-ventas/registrarVenta', methods=['POST'])
def registrar_venta():
    """
    Registra una venta en el sistema de compras-ventas.
    ---
    parameters:
      - name: peticion
        in: body
        required: true
        schema:
          type: object
          properties:
            emisor:
              type: object
              properties:
                nombre:
                  type: string
                identificacion:
                  type: string
                direccion:
                  type: string
                telefono:
                  type: string
            cliente:
              type: object
              properties:
                nombre:
                  type: string
                identificacion:
                  type: string
                direccion:
                  type: string
            condicion_venta:
              type: string
            forma_pago:
              type: string
              enum: [contado, credito, transferencia]
            productos:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  cantidad:
                    type: integer
                  nombre:
                    type: string
                  precio:
                    type: number
    responses:
      200:
        description: Venta registrada exitosamente.
        schema:
          type: object
          properties:
            mensaje:
              type: string
              example: "Venta registrada correctamente"
    """
    return compras_ventas_controller.registrar_venta()

if __name__ == '__main__':
    app.run(debug=True, host=socket.gethostbyname(socket.gethostname()), port=8000)