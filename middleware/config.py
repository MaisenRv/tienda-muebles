URLS ={
    'contabilidad':{
        'generarFactura': 'http://172.20.0.6:8000/contabilidad/generarFactura',
        'recibirFactura': 'http://172.20.0.6:8000/contabilidad/recibirFactura'
    },
    'transportador':{
        'ordenarTransporte': 'http://172.20.0.5:8000/transportador/ordenarTransporte',
    },
    'tienda':{
        'atenderCliente': 'http://172.20.0.3:8000/tienda/atenderCliente',
    },
    'inventario':{
        'cargarProductos': 'http://172.20.0.4:8000/inventario/cargarProductos',
        'validarProductos': 'http://172.20.0.4:8000/inventario/validarProductos',
        'cargarRequerimientosProductos': 'http://172.20.0.4:8000/inventario/cargarRequerimientosProductos',
        'actualizarInventario': 'http://172.20.0.4:8000/inventario/actualizarInventario'
    },
    'compra-venta':{
        'registarCompra': 'http://172.20.0.7:8000/compras-ventas/registrarCompra',
        'registarVenta': 'http://172.20.0.7:8000/compras-ventas/registrarVenta',
    },
    'atencion-proveedor':{
        'atenderProveedor': 'http://172.20.0.8:8000/atencion-proveedor/atenderProveedor',
    }
}