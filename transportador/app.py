from flask import Flask
import socket
from flasgger import Swagger

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
def ordenar_transporte():
    """
    Genera una orden de transporte para un producto.
    ---
    tags:
      - Transportador
    parameters:
      - name: data
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
                direccion:
                  type: string
                identificacion:
                  type: string
            cliente:
              type: object
              properties:
                nombre:
                  type: string
                direccion:
                  type: string
                identificacion:
                  type: string
            productos:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  cantidad:
                    type: integer
                  precio_unitario:
                    type: number
                  nombre:
                    type: string
    responses:
      200:
        description: Orden de transporte generada exitosamente
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Orden de transporte generada exitosamente"
    """
    return transportador_controller.ordenar_transporte()

if __name__ == '__main__':
    app.run(debug=True,host=socket.gethostbyname(socket.gethostname()), port=8000)