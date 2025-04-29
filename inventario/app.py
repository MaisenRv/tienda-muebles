from flask import Flask
import socket

from src.controllers.inventario_controller import InventarioController

app = Flask(__name__)

inventario_controller = InventarioController()

app.add_url_rule('/inventario/actualizarInventario', view_func=inventario_controller.actualizar_inventario, methods=['POST'])
app.add_url_rule('/inventario/cargarProductos', view_func=inventario_controller.cargar_productos, methods=['GET'])
app.add_url_rule('/inventario/validarProductos', view_func=inventario_controller.validar_productos, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True,host=socket.gethostbyname(socket.gethostname()), port=8000)