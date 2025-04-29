from flask import request, jsonify
from datetime import date
from collections import Counter
from src.dao.contabilidad_dao import ContabilidadDAO

class ContabilidadController:
    __values_invoice_input = ['emisor', 'cliente', 'condicion_venta', 'forma_pago', 'productos']
    __contabilidad_dao = ContabilidadDAO()  


    def generar_factura(self):
        data = request.get_json()
        checked =  self.__check_invoice_data(data)

        if not checked['valid']:
            return jsonify(checked), 400
        
        totals = self.__calculate_total_values(data['productos'])
        invoice_completed = self.__format_invoice( data, totals)
        self.__contabilidad_dao.add_invoice(invoice_completed, 'Ventas')

        return jsonify(invoice_completed), 200



    def recibir_factura(self):
        data = request.get_json()
        self.__contabilidad_dao.add_invoice(data, "Compras")
        return jsonify({"save":"correct",**data}), 200

    def __format_invoice(self, data, totales):
        invoice = {
            "factura_numero": self.__generate_invoice_number(),
            "fecha_emision": date.today().isoformat(),
            **data,
            **totales,
        }
        return invoice

    def __calculate_total_values(self, products):
        subtotal = 0
        iva = 0
        total = 0
        for product in products:
            subtotal += product['precio_unitario'] * product['cantidad']
        iva = subtotal * 0.19
        total = subtotal + iva

        return { "subtotal":subtotal , "iva": iva, "total": total }
        
    def __generate_invoice_number(self):
        consecutive_number = self.__contabilidad_dao.get_last_number() # Placeholder for the last invoice number
        consecutive_number = int(consecutive_number[1:]) + 1
        return f'F{consecutive_number:05}'

    def __check_invoice_data(self, data: dict) -> dict:
        messaje = {'valid': True}
        keys = data.keys()

        if set(self.__values_invoice_input) != set(keys): 
            counter_values = Counter(self.__values_invoice_input)
            counter_keys = Counter(keys)
            extra = counter_keys - counter_values
            missing = counter_values - counter_keys

            error_message = ''
            if len(list(extra.elements())) != 0:
                error_message += f'Estos elementos sobran {list(extra.elements())}. '
            if len(list(missing.elements())) != 0:
                error_message += f'Estos elementos faltan {list(missing.elements())}. '

            messaje['valid'] = False
            messaje['error_message'] = error_message
        
        if len(data['productos']) == 0:
            messaje['valid'] = False
            messaje['error_message'] = 'La lista de productos esta vacia -> items: []'
        return messaje