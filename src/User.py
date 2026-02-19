from json import JSONDecodeError
from src.Pokemon import Pokemon
from os import path
if __name__ == "__main__":
    from DataManagement import DataManagement
else:
    from src.DataManagement import DataManagement
class User:
    def __init__(self, is_new:bool, id = None, name_input = "", main: str= None):
        self.__is_new = is_new
        self.__data = DataManagement()

        if self.__is_new == True:
            self.__id = id
            self.__name = name_input
            self.main = main
            self.pokedex = []

            self.__create_user_save()
        else:
            self.__id = id
            self.__name = None
            self.main = None
            self.pokedex = None

            self.__load_user()

    def __create_user_save(self):
        data = {}
        
        if path.exists(self.__data.get_pokedex_path()):
            try:
                data = self.__data.read_pokedexs()
            except JSONDecodeError:
                data = {}
        else:
            self.__data.write_pokedexs("")

        existing_ids = []
        for key in data.keys():
            try:
                uid = int(key[0])
                existing_ids.append(uid)
            except ValueError:
                pass

        if existing_ids:
            self.__id = max(existing_ids) + 1
        else:
            self.__id = 1

        user_key = f"{self.__id}"
        data[user_key] = {
            "name": self.__name,
            "pokedex": [],
            "main": self.main,
        }

        self.__data.write_pokedexs(data)

    def delete_user(self):
        if not path.exists(self.__data.get_pokedex_path()):
            self.__data.write_pokedexs("")
            print("File cannot be deleted : Fresh file.")

        data = self.__data.read_pokedexs()

        user_key = f"{self.__id}"
        
        if user_key in data:
            del data[user_key]
            self.__data.write_pokedexs(data)
            
            self.__id = None
            self.pokedex = {}
        else:
            print("The player you try to delete doesn't exist. Please try again.")

    def get_id(self):
        return self.__id
        
    def __load_user(self):
        data = self.__data.read_pokedexs()
        save_id = f"{self.__id}"

        if save_id in data:
            for d in data:
                if save_id == d:
                    self.__id = d

                    self.__name = data[d]["name"]
                    self.pokedex = data[d]["pokedex"]
                    self.main = data[d]["main"]
        else:
            print("Error : id not recognized. Please try again.")

    def update_pokemon(self, pokemon_to_update: Pokemon):
        for pokemon in self.pokedex:
            if pokemon_to_update.get_name() == pokemon["name"]["fr"]:
                pokemon = pokemon_to_update.pokemon_to_json()

    def capture_pokemon(self, pokemon_to_capture: Pokemon):
        for pokemon in self.pokedex:
            if pokemon_to_capture.get_name() == pokemon["name"]:
                pokemon = pokemon_to_capture.pokemon_to_json()
        else:
            self.pokedex.append(pokemon_to_capture.pokemon_to_json())

    def save_pokedex(self):
        all_datas = self.__data.read_pokedexs()
        all_datas[f"{self.__id}"]["pokedex"] = self.pokedex
        self.__data.write_pokedexs(all_datas)