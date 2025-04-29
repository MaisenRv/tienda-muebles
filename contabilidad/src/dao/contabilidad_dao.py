import json

class ContabilidadDAO:
    __DB_PATH = 'src/db/facturas.json'

    def get_all(self):
        with open(self.__DB_PATH, 'r') as f:
            return json.load(f)

    def save_all(self, data):
        with open(self.__DB_PATH, 'w') as f:
            json.dump(data, f)

    def add_invoice(self, invoice:dict, type:str):
        invoices = self.get_all()
        invoices[type].append(invoice)
        self.save_all(invoices)

    def get_last_number(self):
        invoices = self.get_all()
        last_number = ""
        if len(invoices['Ventas']) != 0:
            last_number = invoices['Ventas'][-1]['factura_numero']
        else:
            last_number = "F00000"
        return last_number