from flask import Flask
import socket
from flasgger import Swagger

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
def atender_cliente():
    """
    Atender a un cliente en la tienda.
    ---
    tags:
      - Tienda
    parameters:
      - name: data
        in: body
        required: true
        schema:
          type: object
          required:
            - peticion
          properties:
            peticion:
              type: string
              description: Acción que quiere realizar el cliente
              enum:
                - comprar
                - mirar_productos
            cliente:
              type: object
              properties:
                nombre:
                  type: string
                direccion:
                  type: string
                identificacion:
                  type: string
            condicion_venta:
              type: string
              enum: ["contado", "credito"]
            forma_pago:
              type: string
              enum: ["efectivo", "credito", "cheque", "transferencia bancaria"]
            productos:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    description: ID del producto
                  cantidad:
                    type: integer
                    description: Cantidad del producto
    """
    return tienda_controller.atender_cliente()


if __name__ == '__main__':
    app.run(debug=True,host=socket.gethostbyname(socket.gethostname()), port=8000)