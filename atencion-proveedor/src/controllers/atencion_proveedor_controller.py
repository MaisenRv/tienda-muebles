from flask import jsonify

class AtencionProveedorController:
    def atender_proveedor(self):
        return jsonify({"message": "Atencion Proveedor"}), 200