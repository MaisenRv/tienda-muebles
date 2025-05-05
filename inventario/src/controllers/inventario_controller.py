from flask import request, jsonify
from src.dao.inventario_dao import InventarioDAO

class InventarioController:
    __inventario_dao = InventarioDAO()

    def cargar_productos(self):
        return self.__inventario_dao.get_all()["productos"]
    
    def cargar_requerimientos_productos(self):
        productos_requeridos = []
        productos_list = self.__inventario_dao.get_all()["productos"]
        for producto in productos_list:
            if producto["cantidad"] < 10:
                producto["cantidad_requerida"] = 10 - producto["cantidad"]
                del producto["cantidad"]
                del producto["precio_unitario"]
                productos_requeridos.append(producto)
        return jsonify({"productos_requeridos": productos_requeridos}), 200

        

    def validar_productos(self):
        data = request.get_json()
        productos_list = self.__inventario_dao.get_all()["productos"]
        productos = {p["id"]: p for p in productos_list}
        productos_validos = []
        for producto in data:
            if producto["id"] not in productos:
                return jsonify({"error": f'El producto con el id {producto["id"]} no existe' }), 400
            if producto["cantidad"] > productos[producto["id"]]["cantidad"]:
                return jsonify({"error": f'No hay suficiente cantidad del producto con el id {producto["id"]}'}), 400
            productos_validos.append(productos[producto["id"]])
            
        return jsonify({"productos_validos": productos_validos}), 200
    
    def actualizar_inventario(self):
        data = request.get_json()
        self.__inventario_dao.update_products(data["productos"], data["tipo"])
        for producto in data["productos"]:
            self.__inventario_dao.add(
                {
                    "operacion":data["tipo"],
                    "id":producto["id"], 
                    "cantidad": producto["cantidad"]
                },
                "inventario"
            )
        return jsonify({"mensaje": "Inventario actualizado correctamente","data":data}), 200