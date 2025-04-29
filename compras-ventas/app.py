from flask import Flask
import socket

from src.controllers.compras_ventas_controller import ComprasVentasController

app = Flask(__name__)

compras_ventas_controller = ComprasVentasController()

app.add_url_rule('/compras-ventas/registrarCompra', view_func=compras_ventas_controller.registrar_compra, methods=['POST'])
app.add_url_rule('/compras-ventas/registrarVenta', view_func=compras_ventas_controller.registrar_venta, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, host=socket.gethostbyname(socket.gethostname()), port=8000)