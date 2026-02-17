from src.DataManagement import DataManagement
from os import path, pardir
from pygame import image
class Pokemon:
    def __init__(self, 
                 name : str, 
                 max_hp: int, 
                 attack: int, 
                 defense: int,
                 speed: int,
                 types : dict,
                 evolution: dict,
                 xp = 0, 
                 max_stats = None,
                 level = 1,
                 is_main = False,
                 ):
        self.__data_management = DataManagement()
        self.__BASE_DIR = path.dirname(path.abspath(__file__))
        self.__data_all = self.__data_management.load_pokemons()
        self.__data = None
        self.__name = name
        self.__id = self.get_id_per_name()
        self.__max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.__types = types
        self.__evolution = evolution
        self.__sprites = self.get_sprite
        self.__max_stats = max_stats
        self.__xp = xp
        self.__level = level
        self.ko = False
        self.is_main = is_main
        self.json_pokemon = self.pokemon_to_json
        self.__xp_levels_cub = [0]
        for n in range(1, 100):
            self.__xp_levels_cub.append(int(n ** 3))

    # ------ CHECK XP AND LEVEL UP ------ #    
    def check_xp(self):
        for n in range(self.__level, 100):
            if self.__xp > self.__xp_levels_cub[n]:
                self.__level_up()
        self.pokemon_to_json

    def __level_up(self): 
        self.__level += 1
        self.__increase_hp()
        self.__increase_atk()
        self.__increase_def()
        self.__increase_speed()
        self.__evolve()
        return None
    # ------ END CHECK XP AND LEVEL UP ------ #

    # ------ INCREASE ------ #
    def __increase_hp(self):
        if self.hp + 1 < self.__max_stats['hp']:
            self.hp += 1
            self.__max_hp += 1
        return None

    def __increase_atk(self):
        if self.__level % 2 == 0 and self.attack  + 2 < self.__max_stats['atk']:
            self.attack += 2
        return None
    
    def __increase_def(self):
        if self.__level % 2 != 0 and self.defense  + 2 < self.__max_stats['def']:
            self.defense += 2
        return None

    def __increase_speed(self):
        if self.speed + 1 < self.__max_stats['vit']:
            self.speed += 1
        return None
    # ------ END INCREASE ------ #

    # ------ GET SOMETHING ------ #
    def get_max_hp(self):
        return self.__max_hp
    
    def get_level(self):
        return self.__level

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_id_per_name(self):
        for entry in self.__data_all:
            if entry['name']['fr'] == self.__name:
                return entry['pokedex_id']
    
    def get_sprite(self):
        sprite_front = path.join(self.__BASE_DIR, pardir, "assets", "images", "sprites", "fronts", f'{self.__id}.png')
        sprite_back = path.join(self.__BASE_DIR, pardir, "assets", "images", "sprites", "backs", f'{self.__id}.png')
        sprites = {"front": image.load(sprite_front).convert_alpha(),"back": image.load(sprite_back).convert_alpha()}
        return sprites
        
    # ------ END GET SOMETHING ------ #            
    # ------ EVOLVE ------ # 
    def __evolve(self):
        if not self.__evolution:
            return None
         
        if isinstance(self.__evolution, list):

            evo_level = self.__evolution[0]["condition"]
            evo_id = self.__evolution[0]["pokedex_id"]

            if evo_level and evo_id and self.__level >= evo_level:
                
                # Looking for the data of poke evo
                self.__data = self.__data_all[evo_id -1 ]

                # Change max stats to init stats of the evo
                self.__max_stats = self.__data['stats']
            
                # Change all stats and the name for the new poke
                
                self.__name = self.__data['name']['fr']
                self.hp = self.__max_stats['hp']
                self.__max_hp = self.__max_stats['hp']
                self.attack = self.__max_stats['atk']
                self.defense = self.__max_stats['def']
                self.speed = self.__max_stats['vit']
                self.__types = self.__data['types'] # getter ?
                # change id to reload sprite
                self.__id = self.get_id_per_name()
                # change sprite 
                self.__sprites = self.get_sprite()

                # Check if poke had a next.....
                self.__evolution = self.__data['evolution']['next']
            
                # if next exist need to change evolution (below) / and max_stats(if exist or not)
                if  isinstance(self.__evolution, list): 
                    self.__max_stats = self.__data_all[evo_id]['stats']
                else:
                    self.__max_stats = {"hp": 1000,"atk": 1000,"def": 1000,"spe_atk": 1000,"spe_def": 1000,"vit": 1000} 
    
    # ------ END EVOLVE ------ #

    # ------ JSON ------ #

    def pokemon_to_json(self):
        json_pokemon = {
            "pokedex_id": self.__id,
            "name": self.__name,
            "hp": self.__max_hp,
            "atk": self.attack,
            "def": self.defense,
            "vit": self.speed,
            "types" : self.__types,
            "evolution": self.__evolution,
            "sprites": self.__sprites,
            "xp": self.__xp, 
            "max_stats" :self.__max_stats,
            "level": self.__level,
            "main": self.is_main
        }
        return json_pokemon

    # ------ END JSON ------ #

if __name__ == "__main__":
    poke_test = Pokemon('Bulbizarre',
                        45,
                        42,
                        40,
                        40,
                        [{'name': 'Plante'},{'name': 'Poison'}],
                        [{"pokedex_id": 2,"name": "Herbizarre","condition": 16  },{"pokedex_id": 3,"name": "Florizarre","condition": 32}],
                        3380,
                        {"hp": 60,"atk": 62,"def": 63,"spe_atk": 80,"spe_def": 80,"vit": 60},
                        15
                        )
    print(poke_test.id)
    #1ere evo
    #poke_test.check_xp()
    #print(poke_test)
    #poke_test.xp = 30000
    ##2ieme evo
    #poke_test.check_xp()
    #print(poke_test)
    #poke_test.xp = 43000
    ##Plus test
    #poke_test.check_xp()
    #print(poke_test)
    #poke_test_2 = Pokemon('Herbizarre',
    #                    45,
    #                    42,
    #                    40,
    #                    40,
    #                    [{'name': 'Plante'},{'name': 'Poison'}],
    #                    [{"pokedex_id": 3,"name": "Florizarre","condition": 32}],
    #                    30000,
    #                    {"hp": 80,"atk": 82,"def": 83,"spe_atk": 1000,"spe_def": 100,"vit": 20},
    #                    31
    #                    )
    #poke_test_2.check_xp()
    #print(poke_test_2)
#
    #poke_test_3 = Pokemon('Florizarre',
    #                    45,
    #                    42,
    #                    40,
    #                    40,
    #                    [{'name': 'Plante'},{'name': 'Poison'}],
    #                    None,
    #                    30000,
    #                    {"hp": 1000,"atk": 1000,"def": 1000,"spe_atk": 1000,"spe_def": 1000,"vit": 1000},
    #                    32
    #                    )
    #poke_test_3.check_xp()
    #print(poke_test_3)
    #