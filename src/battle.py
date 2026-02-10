from json import load, dump
from random import randint
from PIL import Image

class Battle:
    def __init__(self, user_pkm):
        self.__turn = 0
        self.user_pkm = user_pkm
        self.user_pokedex = self.get_user_pokedex()
        self.wild_pokemon = self.choose_rdm_pokemon()
        self.weakness_ratios = self.get_weakness_ratios()

    def get_user_pokedex(self):
        with open("data/pokedex.json", "r") as f:
            self.user_pokedex = load(f)
            
    def get_weakness_ratios(self):
        data = None
        with open("data/types.json", "r") as f:
            data = load(f[self.user_pkm.types]), load(f[self.wild_pokemon.types])

        self.weakness_ratios = data

    def choose_rdm_pokemon(self):
        data = {}
        rdm = randint(1, 151)

        with open("data/pokemon.json", "r") as f:
            data = load(f)
        for pkm in data:
            if pkm[rdm] in data:
                self.wild_pokemon = Pokemon(pkm["name"]["fr"], pkm["stats"]["hp"], pkm["stats"]["atk"], pkm["stats"]["def"], pkm["stats"]["vit"], pkm["types"], 0, Image.open(f"../assets/{str(rdm)}.png"))


    def check_turn(self):
        if self.__turn == 0:
            if self.user_pkm.speed > self.wild_pokemon.speed:
                self.__turn = self.user_pkm
            elif self.user_pkm.speed < self.wild_pokemon.speed:
                self.__turn = self.wild_pokemon
            else:
                random = randint(1, 2)
                if random == 1:
                    self.__turn = self.user_pkm
                else: 
                    self.__turn = self.wild_pokemon
        else:
            if self.__turn == self.user_pkm:
                self.__turn = self.wild_pokemon
            else:
                self.__turn = self.user_pkm


    # def assign_attack_multi(self):
    #     if 
    #     check1 = self.weakness_ratios[self.user_pkm.types]
