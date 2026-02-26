
import json
from os import path, pardir



class DataManagement:
    
    def __init__(self):
        BASE_DIR = path.dirname(path.abspath(__file__))
        self.__pokedex_path = path.join(BASE_DIR,pardir, "data", "pokedexs.json")
        self.__pokemons_path = path.join(BASE_DIR,pardir, "data", 'pokemons.json')
        self.__weakness_ratios_path = path.join(BASE_DIR,pardir, "data",'weakness_ratios.json')
        self.__pokedex_data = self.read_pokedexs_json()
        self.__pokemons_data = self.read_pokemons_json()
        self.__weakness_ratios_data = {}
        self.__pokemon_data = {}
    
    def get_pokedex_path(self):
        return self.__pokedex_path

    # Load pokedex
    def read_pokedexs_json(self):
        with open (self.__pokedex_path,'r', encoding="utf-8") as f:
            self.__pokedex_data = json.load(f)
        return self.__pokedex_data
    
    # Load all pokemons
    def read_pokemons_json(self):
        with open (self.__pokemons_path,'r', encoding="utf-8") as f:
            self.__pokemons_data = json.load(f)
        return self.__pokemons_data

    # Load a pokemon by a ID
    def load_pokemon_by_id(self, id):
        for entry in self.__pokedex_data:
            if entry['pokedex_id'] == id:
                self.__pokemon_data = entry[id - 1]
                return self.__pokemon_data

    # Load weakness
    def read_weakness_ratios_json(self):
        with open (self.__weakness_ratios_path,'r', encoding="utf-8") as f:
            self.__weakness_ratios_data = json.load(f)
        return self.__weakness_ratios_data
    
    # Save pokedex
    def write_pokedexs_json(self, save):
        with open (self.__pokedex_path,'w', encoding="utf-8") as f:
            json.dump(save, f, indent = 4)

    # Save pokemons
    def write_pokemons_json(self, pokemons):
        with open (self.__pokemons_path,'w', encoding="utf-8") as f:
            json.dump(pokemons, f, indent = 4)