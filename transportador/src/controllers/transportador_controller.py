from flask import request, jsonify
from src.dao.transportador_dao import TransportadorDAO

class TransportadorController:
    __transportador_dao = TransportadorDAO()
    def ordenar_transporte(self):
        data = request.get_json()
        self.__transportador_dao.add(data, "transporte")
        return jsonify({"mensaje": "Orden de transporte generada exitosamente","data":data}), 200
        