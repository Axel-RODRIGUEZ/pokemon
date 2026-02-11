from json import load
from random import randint
from PIL import Image
from pokemon import Pokemon
from os import path

class Battle:
    def __init__(self, user_pkm):
        self.__turn = 0
        self.user_pkm = user_pkm
        self.user_pokedex = self.get_user_pokedex()
        self.wild_pokemon = self.choose_rdm_pokemon()
        # self.weakness_ratios = self.get_weakness_ratios()

    def get_user_pokedex(self):
        try:
            with open("data/pokedex.json", "r", encoding='utf-8') as f:
                return load(f)
        except FileNotFoundError:
            return []
            
    # def get_weakness_ratios(self):
    #     data = None
    #     with open("data/types.json", "r") as f:
    #         data = load(f[self.user_pkm.types]), load(f[self.wild_pokemon.types])

    #     self.weakness_ratios = data

    def choose_rdm_pokemon(self):
        rdm = randint(0, 150)
        
        with open("data/pokemon.json", "r", encoding='utf-8') as f:
            data = load(f)
            
            pkm = data[rdm] 
            
            try:
                script_dir = path.dirname(path.abspath(__file__))
                sprites_path = path.join(script_dir, "..", "assets", "images", "sprites", "fronts", f"{rdm + 1}.png")

                img = Image.open(sprites_path)
            except:
                img = None

            wild_pkm = Pokemon(
                name=pkm["name"]["fr"],
                max_hp=pkm["stats"]["hp"],
                attack=pkm["stats"]["atk"],
                defense=pkm["stats"]["def"],
                speed=pkm["stats"]["vit"],
                types=pkm["types"], 
                sprite=img
            )
            
            return wild_pkm


    def check_turn(self):
        if self.__turn == 0:
            if self.user_pkm.speed > self.wild_pokemon.speed:
                self.__turn = self.user_pkm
            elif self.user_pkm.speed < self.wild_pokemon.speed:
                self.__turn = self.wild_pokemon
            else:
                self.__turn = self.user_pkm if randint(1, 2) == 1 else self.wild_pokemon
        else:
            self.__turn = self.wild_pokemon if self.__turn == self.user_pkm else self.user_pkm


    # def assign_attack_multi(self):
    #     if 
    #     check1 = self.weakness_ratios[self.user_pkm.types]

battle = Battle("test")

mon_starter = Pokemon(
    name="Dracaufeu", 
    max_hp=100, attack=80, defense=70, speed=100, 
    types=[{"name": "Feu"}] 
)

battle = Battle(mon_starter)

print(f"Combat lancé contre : {battle.wild_pokemon.name}")
print(f"HP du sauvage : {battle.wild_pokemon.max_hp}")

battle.wild_pokemon.sprite.show()