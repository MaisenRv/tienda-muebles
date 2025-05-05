from flask import Flask
import socket
from flasgger import Swagger, swag_from

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
@swag_from('src/docs/registrar_compra.yml')
def registrar_compra():
    return compras_ventas_controller.registrar_compra()

@app.route('/compras-ventas/registrarVenta', methods=['POST'])
@swag_from('src/docs/registrar_venta.yml')
def registrar_venta():
    return compras_ventas_controller.registrar_venta()

if __name__ == '__main__':
    app.run(debug=True, host=socket.gethostbyname(socket.gethostname()), port=8000)