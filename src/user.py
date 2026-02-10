import json
import os

class User:
    def __init__(self, name_input):
        self.__name = name_input
        self.__save_id = None
        self.pokedex = {}
        self.json_file = "data/pokedex.json"

        self.create_user_save()

    def create_user_save(self):
        data = {}
        
        if os.path.exists(self.json_file):
            try:
                with open(self.json_file, "r") as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                data = {}

        existing_ids = []
        for key in data.keys():
            if key.startswith("save_id_"):
                try:
                    uid = int(key.split("_")[-1])
                    existing_ids.append(uid)
                except ValueError:
                    pass

        if existing_ids:
            self.__save_id = max(existing_ids) + 1
        else:
            self.__save_id = 1

        user_key = f"save_id_{self.__save_id}"
        data[user_key] = {
            "name": self.__name,
            "pokemons": {}
        }

        with open(self.json_file, "w") as f:
            json.dump(data, f, indent=4)

    def delete_user(self):
        if not os.path.exists(self.json_file):
            return

        with open(self.json_file, "r") as f:
            data = json.load(f)

        user_key = f"save_id_{self.__save_id}"
        
        if user_key in data:
            del data[user_key]
            with open(self.json_file, "w") as f:
                json.dump(data, f, indent=4)
            
            self.__save_id = None
            self.pokedex = {}

    def get_save_id(self):
        return self.__save_id