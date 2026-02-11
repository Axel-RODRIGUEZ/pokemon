
import json
from os import path, pardir



class DataManagement:
    
    def __init__(self):
        BASE_DIR = path.dirname(path.abspath(__file__))
        self.__pokedex_path = path.join(BASE_DIR,pardir, "data", "pokedex.json")
        self.__pokemon_path = path.join(BASE_DIR,pardir, "data", 'pokemon.json')
        self.__weaknes_ratio_path = path.join(BASE_DIR,pardir, "data",'weakness_ratio.json')
        self.__pokedex_data = {}
        self.__pokemon_data = {}
        self.__weaknes_ratio_data = {}
    
    #Load pokedex
    def load_pokedex(self):
        with open (self.__pokedex_path,'r', encoding="utf-8") as f:
            self.__pokedex_data = json.load(f)
        return self.__pokedex_data
    
    #Load pokemon
    def load_pokemon(self):
        with open (self.__pokemon_path,'r', encoding="utf-8") as f:
            self.__pokemon_data = json.load(f)
        return self.__pokemon_data

    #Load weakness
    def load_weakness_ratio(self):
        with open (self.__weaknes_ratio_path,'r', encoding="utf-8") as f:
            self.__weaknes_ratio_data = json.load(f)
        return self.__weaknes_ratio_data
    
    def save_pokedex(self,):
        with open (self.__pokedex_path,'r', encoding="utf-8") as f:
            json.dump(self.__pokedex_data, f, indent = 4)
