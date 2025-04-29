import json
class ComprasVentasDAO:
    __DB_PATH = 'src/db/compras-ventas.json'

    def save_all(self, data):
        with open(self.__DB_PATH, 'w') as f:
            json.dump(data, f)
    def get_all(self):
        with open(self.__DB_PATH, 'r') as f:
            data = json.load(f)
        return data

    def add(self, item:dict, type:str):
        items = self.get_all()
        items[type].append(item)
        self.save_all(items)
