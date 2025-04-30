from flask import request, jsonify
import requests
from config import URLS

class MiddlewareController:
    def clientes(self):
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
            registrar_venta = requests.post(URLS['compra-venta']['registarVenta'], json=res)
            if registrar_venta.status_code == 400:
                return registrar_venta.json(), registrar_venta.status_code
            
            # Genera la factura en el componente de contabilidad
            del res["tipo"]
            del res["peticion"]
            generar_factura = requests.post(URLS['contabilidad']['generarFactura'], json=res)
            
            # Actualiza el inventario
            actualizar_inventario = requests.post(URLS['inventario']['actualizarInventario'], json={"productos":res["productos"], "tipo": "venta"})

            #Ordena el transporte
            ordenar_transporte = requests.post(URLS['transportador']['ordenarTransporte'], json={"cliente":res["cliente"], "productos": res["productos"], "emisor": res["emisor"]})
            res["mesaje_ventas_compras"] = registrar_venta.json()["mensaje"]
            res["factura"] = generar_factura.json()
            res["mesaje_inventario"] = actualizar_inventario.json()["mensaje"]
            res["mesaje_transporte"] = ordenar_transporte.json()["mensaje"]

            del res["condicion_venta"]
            del res["forma_pago"]
            del res["productos"]
            return res, 200
        return tienda_resquest.json(), tienda_resquest.status_code

    def proveedores(self):
        data = request.get_json()
        atencion_proveedor_resquest = requests.post(URLS['atencion-proveedor']['atenderProveedor'], json=data)
        return atencion_proveedor_resquest.json(), atencion_proveedor_resquest.status_code

        
        