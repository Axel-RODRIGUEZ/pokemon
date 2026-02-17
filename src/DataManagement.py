
import json
from os import path, pardir



class DataManagement:
    
    def __init__(self):
        BASE_DIR = path.dirname(path.abspath(__file__))
        self.__pokedex_path = path.join(BASE_DIR,pardir, "data", "pokedexs.json")
        self.__pokemon_path = path.join(BASE_DIR,pardir, "data", 'pokemon.json')
        self.__weaknes_ratio_path = path.join(BASE_DIR,pardir, "data",'weakness_ratio.json')
        self.__pokedex_data = self.load_pokedexs()
        self.__pokemons_data = self.load_pokemons()
        self.__weaknes_ratio_data = {}
        self.__pokemon_data = {}
    
    def get_pokedex_path(self):
        return self.__pokedex_path

    # Load pokedex
    def load_pokedexs(self):
        with open (self.__pokedex_path,'r', encoding="utf-8") as f:
            self.__pokedex_data = json.load(f)
        return self.__pokedex_data
    
    # Load all pokemons
    def load_pokemons(self):
        with open (self.__pokemon_path,'r', encoding="utf-8") as f:
            self.__pokemons_data = json.load(f)
        return self.__pokemons_data

    # Load a pokemon by a ID
    def load_pokemon_by_id(self, id):
        for entry in self.__pokedex_data:
            if entry['pokedex_id'] == id:
                self.__pokemon_data = entry[id - 1]
                return self.__pokemon_data

    # Load weakness
    def load_weakness_ratio(self):
        with open (self.__weaknes_ratio_path,'r', encoding="utf-8") as f:
            self.__weaknes_ratio_data = json.load(f)
        return self.__weaknes_ratio_data
    
    # Save pokedex
    def save_pokedex(self, save):
        with open (self.__pokedex_path,'w', encoding="utf-8") as f:
            json.dump(save, f, indent = 4)
