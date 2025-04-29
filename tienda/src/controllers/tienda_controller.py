from flask import request, jsonify

class TiendaController:
    __informacion = {
        "nombre": "Tienda de muebles",
        "direccion": "Calle Falsa 123",
        "telefono": "123456789",
        "identificacion": "123456789",
    }
    def atender_cliente(self):
        data = request.get_json()

        if 'peticion' not in data:
            return jsonify({"error": "Falta el campo 'peticion' en la solicitud"}), 200

        if data['peticion'] == 'mirar_productos':
            return jsonify({"tipo":"mirar_productos"}), 200
        
        elif data['peticion'] == 'comprar':
            if 'cliente' not in data:
                return jsonify({"error":"Falta el campo 'cliente' en la solicutud"}), 200
            if 'productos' not in data:
                return jsonify({"error":"Falta el campo 'productos' en la solicitud"}), 200
            if data['productos'] == []:
                return jsonify({"error":"El campo 'productos' esta vacio"}), 200
            
            return jsonify({
                "tipo":"compra", 
                "cliente": data['cliente'],
                "emisor":self.__informacion, 
                "productos": data['productos'],
                "condicion_venta": data['condicion_venta'] if 'condicion_venta' in data else None,
                "forma_pago": data['forma_pago'] if 'forma_pago' in data else 'contado'
            }), 200
        
        else:
            return jsonify({"error": "Petición no válida"}), 400
