from json import JSONDecodeError
from src.Pokemon import Pokemon
from os import path
if __name__ == "__main__":
    from DataManagement import DataManagement
else:
    from src.DataManagement import DataManagement
class User:
    def __init__(self, is_new:bool, id = 1, name_input = "", main: str= None):
        self.__is_new = is_new
        self.__data = DataManagement()

        if self.__is_new == True:
            self.__name = name_input
            self.main = main
            self.__save_id = self.__create_user_save()
            self.pokedex = self.__load_pokedex()
        else:
            self.__id = id
            self.__name = None
            self.main = None
            self.__save_id = None
            self.pokedex = None

            self.__load_user()

    def __create_user_save(self):
        data = {}
        
        if path.exists(self.__data.get_pokedex_path()):
            try:
                data = self.__data.load_pokedexs()
            except JSONDecodeError:
                data = {}
        else:
            self.__data.save_pokedex("")

        existing_ids = []
        for key in data.keys():
            try:
                uid = int(key[0])
                existing_ids.append(uid)
            except ValueError:
                pass

        if existing_ids:
            save_id = max(existing_ids) + 1
        else:
            save_id = 1

        user_key = f"{save_id}"
        data[user_key] = {
            "name": self.__name,
            "pokedex": [],
            "main": self.main,
        }

        self.__data.save_pokedex(data)

    def delete_user(self):
        if not path.exists(self.__data.get_pokedex_path()):
            self.__data.save_pokedex("")
            print("File cannot be deleted : Fresh file.")

        data = self.__data.load_pokedexs()

        user_key = f"{self.__save_id}"
        
        if user_key in data:
            del data[user_key]
            self.__data.save_pokedex(data)
            
            self.__save_id = None
            self.pokedex = {}
        else:
            print("The player you try to delete doesn't exist. Please try again.")

    def get_save_id(self):
        return self.__save_id
    
    def __load_pokedex(self):
        pokedex = self.__data.load_pokedexs()
        if pokedex.keys() == self.__save_id:
            return pokedex 
        else: 
            return []
        
    def __load_user(self):
        data = self.__data.load_pokedexs()
        save_id = f"{self.__id}"

        if save_id in data:
            for d in data:
                if save_id == d:
                    self.__save_id = d

                    self.__name = data[d]["name"]
                    self.pokedex = data[d]["pokedex"]
                    self.main = data[d]["main"]
        else:
            print("Error : id not recognized. Please try again.")
