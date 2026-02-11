
import json
from os import path, pardir



class DataManagement:
    
    def __init__(self):
        BASE_DIR = path.dirname(path.abspath(__file__))
        self.pokedex_path = path.join(BASE_DIR,pardir, "data", "pokedex.json")
        self.pokemon_path = path.join(BASE_DIR,pardir, "data", 'pokemon.json')
        self.weaknes_ratio_path = path.join(BASE_DIR,pardir, "data",'weakness_ratio.json')
        self.pokedex_data = {}
        self.pokemon_data = {}
        self.weaknes_ratio_data = {}
    
    #Load pokedex
    def load_pokedex(self):
        with open (self.pokedex_path,'r', encoding="utf-8") as f:
            self.pokedex_data = json.load(f)
        return self.pokedex_data
    
    #Load pokemon
    def load_pokemon(self):
        with open (self.pokemon_path,'r', encoding="utf-8") as f:
            self.pokemon_data = json.load(f)
        return self.pokemon_data

    #Load weakness
    def load_weakness_ratio(self):
        with open (self.weaknes_ratio_path,'r', encoding="utf-8") as f:
            self.weaknes_ratio_data = json.load(f)
        return self.weaknes_ratio_data
    
    def save_pokedex(self,):
        with open (self.pokedex_path,'r', encoding="utf-8") as f:
            json.dump(self.pokedex_data, f, indent = 4)
