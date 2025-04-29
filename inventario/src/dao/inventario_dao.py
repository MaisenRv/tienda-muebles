import json

class InventarioDAO:
    __DB_PATH = 'src/db/inventario.json'
    def get_all(self):
        with open(self.__DB_PATH, 'r') as f:
            return json.load(f)

    def save_all(self, data):
        with open(self.__DB_PATH, 'w') as f:
            json.dump(data, f)

    def update_products(self, data:dict):
        items = self.get_all()
        for element in data:
            for item in items["productos"]:
                if item["id"] == element["id"]:
                    item["cantidad"] -= element["cantidad"]
                    break
        self.save_all(items)
            
    def add(self, item:dict, type:str):
        items = self.get_all()
        items[type].append(item)
        self.save_all(items)
