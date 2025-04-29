from flask import request, jsonify
import requests
from config import URLS

class MiddlewareController:
    def clientes(self):
        """
        Maneja las peticiones relacionadas con los clientes.

        Este método procesa diferentes tipos de peticiones relacionadas con los clientes, como mirar productos o realizar compras.

        Args:
            peticion (dict): Un diccionario que contiene la información de la petición. Puede tener las siguientes estructuras:
                - Para mirar productos:
                {
                    "peticion": "mirar_productos"
                }
                - Para realizar una compra:
                {
                    "peticion": "comprar",
                    "cliente": {
                        "nombre": "jose",
                        "identificacion": "111223141"
                    },
                    "condicion_venta": "contado",
                    "forma_pago": contado | credito | transferencia,
                    ,
                    "productos": [
                        {"id": 1, "cantidad": 2},
                        ...
                    ]
                }

        Returns:
            dict: Un diccionario con la respuesta a la petición. La estructura de la respuesta depende del tipo de petición procesada.

        Raises:
            ValueError: Si la petición no es válida o no contiene los campos requeridos.
        """
        data = request.get_json()
        tienda_resquest = requests.post(URLS['tienda']['atenderCliente'], json=data)
        res = tienda_resquest.json()

        # retorna los productos disponibles
        if 'tipo'in res and res["tipo"] == "mirar_productos":
            productos = requests.get(URLS['inventario']['cargarProductos'])
            return jsonify(productos.json()),200


        if 'tipo'in res and res["tipo"] == "compra":
            # Valida si existen los productos y su cantidad
            validar_productos = requests.post(URLS['inventario']['validarProductos'], json=res["productos"])
            if validar_productos.status_code == 400:
                return validar_productos.json(),validar_productos.status_code
            
            for producto in validar_productos.json()["productos_validos"]:
                for p in res["productos"]:
                    if producto["id"] == p["id"]:
                        p["nombre"] = producto["nombre"]
                        p["precio_unitario"] = producto["precio_unitario"]
            
            # registra la venta en el componente de compras-ventas
            # registrar_venta = requests.post(URLS['compra-venta']['registarVenta'], json=res)
            # if registrar_venta.status_code == 400:
            #     return registrar_venta.json(), registrar_venta.status_code
            
            # Genera la factura en el componente de contabilidad
            # del res["tipo"]
            # del res["peticion"]
            # generar_factura = requests.post(URLS['contabilidad']['generarFactura'], json=res)
            
            # Actualiza el inventario
            # actualizar_inventario = requests.post(URLS['inventario']['actualizarInventario'], json={"productos":res["productos"], "tipo": "venta"})

            #Ordena el transporte
            # ordenar_transporte = requests.post(URLS['transportador']['ordenarTransporte'], json=res)
            
            

        return tienda_resquest.json(), tienda_resquest.status_code
        