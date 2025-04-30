from flask import Flask
import socket
from flasgger import Swagger

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
def clientes():
    """
    Maneja las peticiones relacionadas con los clientes.
    ---
    parameters:
      - name: body
        in: body
        required: true
        description: Peticion del cliente.
        schema:
          type: object
          properties:
            peticion:
              type: string
              example: "compra"
            condicion_venta:
              type: string
              example: "Contado"
            forma_pago:
              type: string
              example: "Efectivo"
            cliente:
              type: object
              properties:
                nombre:
                  type: string
                  example: "Juan Perez"
                direccion:
                  type: string
                  example: "Calle 123"
                identificacion:
                  type: string
                  example: "123456789"
            productos:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  cantidad:
                    type: number
    responses:
      200:
        description: Respuesta exitosa
        schema:
          type: object
          properties:
            cliente:
              type: object
              properties:
                nombre:
                  type: string
                  example: "Juan Perez"
                direccion:
                  type: string
                  example: "Calle 123"
                identificacion:
                  type: string
                  example: "123456789"
            emisor:
              type: object
              properties:
                nombre:
                  type: string
                  example: "Tienda 1"
                direccion:
                  type: string
                  example: "Calle 456"
                identificacion:
                  type: string
                  example: "987654321"
                telefono:
                  type: string
                  example: "123456789"
            factura:
              type: object
              properties:
                cliente:
                  type: object
                  properties:
                    nombre:
                      type: string
                      example: "Juan Perez"
                    direccion:
                      type: string
                      example: "Calle 123"
                    identificacion:
                      type: string
                      example: "123456789"
                emisor:
                  type: object
                  properties:
                    nombre:
                      type: string
                      example: "Tienda 1"
                    direccion:
                      type: string
                      example: "Calle 456"
                    identificacion:
                      type: string
                      example: "987654321"
                    telefono:
                      type: string
                      example: "123456789"
                condicion_venta:
                  type: string
                  example: "Contado"
                forma_pago:
                  type: string
                  example: "Efectivo"
                factura_numero:
                  type: string
                  example: "f00001"
                fecha_emision:
                  type: string
                  example: "2023-10-01"
                productos:
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
                        type: number
                subtotal:
                  type: number
                iva:
                  type: number
                total:
                  type: number
            mensaje_inventario:
                type: string
            mesaje_ventas_compras:
                type: string
            mesaje_transporte:
                type: string        
    """
    return midd_cotroller.clientes()

@app.route('/proveedores', methods=['POST'])
def proveedores():
    """
    """
    return midd_cotroller.proveedores()     
           
if __name__ == '__main__':
    app.run(debug=True,host= socket.gethostbyname(socket.gethostname()),port=8000) 