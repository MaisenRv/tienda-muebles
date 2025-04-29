from flask import request, jsonify
from src.dao.compras_ventas_dao import ComprasVentasDAO
class ComprasVentasController:
    __compra_venta_dao = ComprasVentasDAO()
    def registrar_compra(self):
        pass
    
    def registrar_venta(self):
        data = request.get_json()
        self.__compra_venta_dao.add(data, "ventas")
        return jsonify({"mensaje": "Venta registrada correctamente", "data": data}), 200