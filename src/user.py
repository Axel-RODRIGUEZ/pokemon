from json import JSONDecodeError
from os import path
if __name__ == "__main__":
    from data_management import DataManagement
else:
    from src.data_management import DataManagement
class User:
    def __init__(self, name_input:str, main:object):

        self.__data = DataManagement()
        self.__name = name_input
        self.main = main
        self.__save_id = self.__create_user_save()
        self.pokedex = self.__load_user()

    def __create_user_save(self):
        data = {}
        
        if path.exists(self.__data.pokedex_path):
            try:
                data = self.__data.load_pokedex()
            except JSONDecodeError:
                data = {}
        else:
            self.__data.save_pokedex("")

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
            "pokemons": {},
            "main": self.main,
        }

        self.__data.save_pokedex(data)

    def delete_user(self):
        if not path.exists(self.__data.pokedex_path):
            self.__data.save_pokedex("")
            print("File cannot be deleted : Fresh file.")

        data = self.__data.load_pokedex()

        user_key = f"save_id_{self.__save_id}"
        
        if user_key in data:
            del data[user_key]
            self.__data.save_pokedex(data)
            
            self.__save_id = None
            self.pokedex = {}
        else:
            print("The player you try to delete doesn't exist. Please try again.")

    def get_save_id(self):
        return self.__save_id
    
    def __load_user(self):
        pokedex = self.__data.load_pokedex()
        if pokedex.keys() == self.__save_id:
            return pokedex
        else: 
            return {}