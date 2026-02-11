from json import load, dump, JSONDecodeError
from os import path
from src.data_management import DataManagement
class User:
    def __init__(self, name_input:str):
        self.data = DataManagement()
        self.__name = name_input
        self.pokedex = self.load_user()
        self.json_file = "data/pokedex.json"
        self.main = self.check_main()
        self.__save_id = self.create_user_save()  

    def check_main(self):
        for pokemon in self.pokedex:
            if pokemon.is_main == True:
                self.main = pokemon
            else:
                self.main = None

    def create_user_save(self):
        data = {}
        
        if path.exists(self.json_file):
            try:
                with open(self.json_file, "r") as f:
                    data = load(f)
            except JSONDecodeError:
                data = {}
        else:
            with open(self.json_file, "w") as f:
                dump("", f, indent=4)

        existing_ids = []
        for key in data.keys():
            if key.startswith("save_id_"):
                try:
                    uid = int(key.split("_")[-1])
                    existing_ids.append(uid)
                except ValueError:
                    pass

        if existing_ids:
            save_id = max(existing_ids) + 1
        else:
            save_id = 1

        user_key = f"save_id_{save_id}"
        data[user_key] = {
            "name": self.__name,
            "pokemons": {}
        }

        with open(self.json_file, "w") as f:
            dump(data, f, indent=4)

    def delete_user(self):
        if not path.exists(self.json_file):
            with open(self.json_file, "w") as f:
                dump("", f, indent=4)
                print("File cannot be deleted : Fresh file.")

        with open(self.json_file, "r") as f:
            data = load(f)

        user_key = f"save_id_{self.__save_id}"
        
        if user_key in data:
            del data[user_key]
            with open(self.json_file, "w") as f:
                dump(data, f, indent=4)
            
            self.__save_id = None
            self.pokedex = {}
        else:
            print("The player you try to delete doesn't exist. Please try again.")

    def get_save_id(self):
        return self.__save_id
    
    def load_user(self):
        pokedex = self.data.load_pokedex()
        for i in pokedex:
            if i.keys() == self.__save_id:
                return i
            else: 
                return {}