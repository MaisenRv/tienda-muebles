from flask import Flask
import socket
from flasgger import Swagger

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
def generar_factura():
    """
    Genera una factura
    ---
    tags:
      - Contabilidad
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
                  cantidad:
                    type: integer
                  precio:
                    type: number
                  nombre:
                    type: string
    responses:
      200:
        description: Factura generada correctamente
        schema:
          type: object
          properties:
            factura_numero:
              type: string
            fecha_emision:
              type: string
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
            condicion_venta:
              type: string
            forma_pago:
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
                  precio:
                    type: number
                  nombre:
                    type: string
            subtotal:
              type: number
            iva:
              type: number
            total:
              type: number
    """
    return contabilidad_controller.generar_factura()

@app.route('/contabilidad/recibirFactura', methods=['POST'])
def recibir_factura():
    """
    Recibir una factura
    ---
    tags:
      - Contabilidad
    parameters:
      - name: data
        in: body
        required: true
        schema:
          description: Factura generada correctamente
        schema:
          type: object
          properties:
            factura_numero:
              type: string
            fecha_emision:
              type: string
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
            condicion_venta:
              type: string
            forma_pago:
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
                  precio:
                    type: number
                  nombre:
                    type: string
            subtotal:
              type: number
            iva:
              type: number
            total:
              type: number
    responses:
      200:
        description: Factura recibida exitosamente
        schema:
          type: object
          properties:
            save:
              type: string
    """
    return contabilidad_controller.recibir_factura()


if __name__ == '__main__':
    app.run(debug=True,host=socket.gethostbyname(socket.gethostname()), port=8000)