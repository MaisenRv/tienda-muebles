from flask import jsonify, request

class AtencionProveedorController:
    def atender_proveedor(self):
        data = request.get_json()
        if "peticion" not in data:
            return jsonify({"mensaje": "No se ha enviado la peticion"}), 400
        
        if data["peticion"] == "cargar_requerimientos_productos":
            return jsonify({"tipo": "requerimientos"}), 200
        
        if data["peticion"] == "venta":
            if "factura" not in data:
                return jsonify({"mensaje": "Se necesita un factura"}), 400
            if "productos" not in data["factura"] or len(data["factura"]["productos"]) == 0:
                return jsonify({"mensaje": "Se necesitan productos en la factura"}), 400
            
            return jsonify({"tipo": "venta", "factura":data["factura"]}), 200
        
        return jsonify({"mensaje": "Peticion no valida"}), 400