import json

class InventarioDAO:
    __DB_PATH = 'src/db/inventario.json'
    def get_all(self):
        with open(self.__DB_PATH, 'r') as f:
            return json.load(f)

    # def save_all(self, data):
    #     with open(self.__DB_PATH, 'w') as f:
    #         json.dump(data, f)

    def add(self, item:dict, type:str):
        items = self.get_all()
        items[type].append(item)
        self.save_all(items)
