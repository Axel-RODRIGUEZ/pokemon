from os import path
from json import load
from random import randint
from PIL import Image
if __name__ == "__main__":
    from pokemon import Pokemon
    from user import User
else:
    from src.pokemon import Pokemon
    from src.user import User

class Battle:
    def __init__(self, user:User):
        self.__turn = 0
        self.wild_pokemon = self.__choose_random_pokemon()
        self.user = user
        self.weakness_ratios = self.get_weakness_ratios()
            
    def get_weakness_ratios(self):
        with open("data/types.json", "r") as f:
            type_data = load(f)

        types_dict = {k.lower(): v for k, v in type_data.items()}

        user_ratios = {}
        for t in self.user_pkm.types:
            original_name = t["name"]           
            search_name = original_name.lower() 
            
            data = types_dict.get(search_name)
            user_ratios[original_name] = data
        
        wild_ratios = {}
        for t in self.wild_pokemon.types:
                original_name = t["name"]
                search_name = original_name.lower()
                
                data = types_dict.get(search_name)
                wild_ratios[original_name] = data

        return user_ratios, wild_ratios


    def __choose_random_pokemon(self):
        random = randint(0, 150)
        
        with open("data/pokemon.json", "r", encoding='utf-8') as f:
            data = load(f)
            
            pkm = data[random] 
            
            try:
                script_dir = path.dirname(path.abspath(__file__))
                sprites_path = path.join(script_dir, "..", "assets", "images", "sprites", "fronts", f"{random + 1}.png")

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


    def __check_turn(self):
        if self.__turn == 0:
            if self.user_pkm.speed > self.wild_pokemon.speed:
                self.__turn = self.user_pkm
            elif self.user_pkm.speed < self.wild_pokemon.speed:
                self.__turn = self.wild_pokemon
            else:
                self.__turn = self.user_pkm if randint(1, 2) == 1 else self.wild_pokemon
        else:
            self.__turn = self.wild_pokemon if self.__turn == self.user_pkm else self.user_pkm


    def __assign_attack_multi(self):
        ratios_user, ratios_wild = self.weakness_ratios

        if isinstance(ratios_user, list):
            ratios_user = ratios_user[0]
        if isinstance(ratios_wild, list):
            ratios_wild = ratios_wild[0]

        if self.__turn == self.user_pkm:
            attacker = self.user_pkm
            defender_list = ratios_wild 
        else:
            attacker = self.wild_pokemon
            defender_list = ratios_user

        total_bonus = 0

        for t in attacker.types:
            atk_type_name = t["name"].lower() 
            
            current_type_score = 1
            
            for def_name, def_data in defender_list.items():
                coeff = def_data.get(atk_type_name, 1)
                current_type_score *= coeff
        
            total_bonus += current_type_score

        return total_bonus
    
    def attack(self):
        self.__check_turn()
        attack_multi = self.__assign_attack_multi()

        if self.__turn == self.user_pkm:
            attack = self.user_pkm.attack * attack_multi
            self.wild_pokemon.max_hp -= int(attack)
        else:
            attack = self.wild_pokemon.attack * attack_multi
            self.user_pkm.max_hp -= int(attack)
            
if __name__ == "__main__":

    mon_starter = Pokemon(
        name="Dracaufeu", 
        max_hp=100, attack=80, defense=70, speed=1, 
        types=[{"name": "Feu"}] 
    )

    battle = Battle("test")

    print(f"Combat lancé contre : {battle.wild_pokemon.name}")
    print(f"HP du sauvage : {battle.wild_pokemon.max_hp}")

# battle.wild_pokemon.sprite.show()
 