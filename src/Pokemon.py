from src.DataManagement import DataManagement
from os import path, pardir
from pygame import image
class Pokemon:
    def __init__(self, 
                 name : str, 
                 max_hp: int,
                 hp: int,
                 attack: int, 
                 defense: int,
                 speed: int,
                 types : dict,
                 xp = 0, 
                 level = 1,
                 ):
        self.__data_management = DataManagement()
        self.__BASE_DIR = path.dirname(path.abspath(__file__))
        self.__data_all = self.__data_management.read_pokemons_json()
        self.__name = name
        self.__id = self.get_id_per_name()
        self.__category = self.__load_category()
        self.__max_hp = max_hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = self.__load_special_attack()
        self.special_defense = self.__load_special_defense()
        self.speed = speed
        self.__types = types
        self.__talents = self.__load_talents()
        self.__evolution = self.__load_evolution()
        self.__sprites = self.__load_sprites()
        self.__max_stats = self.__load_max_stats()
        self.__xp = xp
        self.__level = level
        self.ko = False
        self.json_pokemon = self.pokemon_to_json()
        self.__xp_levels_cub = [0]
        for n in range(1, 100):
            self.__xp_levels_cub.append(int(n ** 3))

    # ------ CHECK XP AND LEVEL UP ------ #    
    def check_xp(self):
        for n in range(self.__level, 100):
            if self.__xp > self.__xp_levels_cub[n]:
                self.__level_up()


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
        if (self.hp + 1) < self.__max_stats['max_hp']:
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
    
    def get_xp(self):
        return self.__xp

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_evolution(self):
        return self.__evolution
    
    def increase_xp(self, xp):
        self.__xp += xp
    
    def get_types(self):
        return self.__types
    
    def get_id_per_name(self):
        for entry in self.__data_all:
            if entry['name']['fr'] == self.__name:
                return entry['pokedex_id']
            
    def get_sprites(self):
        return self.__sprites
    
    def __load_sprites(self):
        sprite_front = path.join(self.__BASE_DIR, pardir, "assets", "images", "sprites", "fronts", f'{self.__id}.png')
        sprite_back = path.join(self.__BASE_DIR, pardir, "assets", "images", "sprites", "backs", f'{self.__id}.png')
        sprites = {"front": image.load(sprite_front).convert_alpha(),"back": image.load(sprite_back).convert_alpha()}
        return sprites
    
    def __load_evolution(self):
        for data in self.__data_all:
            if data["pokedex_id"] == self.__id:
                return data["evolution"]
            
    def __load_max_stats(self):
        if isinstance(self.__evolution, dict) and isinstance(self.__evolution["next"], list):
            evolution = self.__evolution["next"]
            evo_id = evolution[0]["pokedex_id"]
            return self.__data_all[evo_id]['stats']
        else:
            max_stats = {"max_hp": 1000,"atk": 1000,"def": 1000,"spe_atk": 1000,"spe_def": 1000,"vit": 1000} 
            return max_stats
    
    def __load_talents(self):
        for data in self.__data_all:
            if data["pokedex_id"] == self.__id:
                return data["talents"]
    
    def __load_category(self):
        for data in self.__data_all:
            if data["pokedex_id"] == self.__id:
                return data["category"]
        
    def __load_special_attack(self):
        for data in self.__data_all:
            if data["pokedex_id"] == self.__id:
                return data["stats"]["spe_atk"]
            
    def __load_special_defense(self):
        for data in self.__data_all:
            if data["pokedex_id"] == self.__id:
                return data["stats"]["spe_def"]
            
    # ------ END GET SOMETHING ------ #            
    # ------ EVOLVE ------ # 
    def __evolve(self):
        if not self.__evolution:
            return None
         
        if isinstance(self.__evolution, dict) and isinstance(self.__evolution["next"], list):

            evo_level = self.__evolution["next"][0]["condition"]
            evo_id = self.__evolution["next"][0]["pokedex_id"]

            if evo_level and evo_id and self.__level >= evo_level:
                
                # Looking for the data of poke evo
                evolution_data = self.__data_all[evo_id-1]
            
                # Change all stats and the name for the new poke
                
                self.__name = evolution_data['name']['fr']
                self.hp = evolution_data['stats']['max_hp']
                self.__max_hp = evolution_data['stats']['max_hp']
                self.attack = evolution_data['stats']['atk']
                self.defense = evolution_data['stats']['def']
                self.special_attack = evolution_data['stats']['spe_atk']
                self.special_defense = evolution_data['stats']['spe_def']
                self.speed = evolution_data['stats']['vit']
                self.__types = evolution_data['types'] # getter ?
                self.__evolution = evolution_data['evolution']
                # change id to reload sprite
                self.__id = evo_id
                # change sprite 
                self.__sprites = self.__load_sprites()
                
            
                # if next exist need to change evolution (below) / and max_stats(if exist or not)
                if isinstance(self.__evolution, dict) and isinstance(self.__evolution["next"], list):
                    evo_id = self.__evolution["next"][0]["pokedex_id"]
                    self.__max_stats = self.__data_all[evo_id-1]['stats']
                else:
                    self.__max_stats = {"max_hp": 1000,"atk": 1000,"def": 1000,"spe_atk": 1000,"spe_def": 1000,"vit": 1000} 
    
    # ------ END EVOLVE ------ #

    # ------ JSON ------ #

    def pokemon_to_json(self):
        json_pokemon = {
            "pokedex_id": self.__id,
            "name": {"fr": self.__name},
            "category": self.__category,
            "stats":{
                "max_hp": self.__max_hp,
                "hp": self.hp,
                "atk": self.attack,
                "spe_atk": self.special_attack,
                "spe_def": self.special_defense,
                "def": self.defense,
                "vit": self.speed,
                "types" : self.__types,
                "xp": self.__xp, 
                "level": self.__level,
                },
            "ko": self.ko,
            "types": self.__types,
            "talents": self.__talents
        }
        return json_pokemon

    # ------ END JSON ------ #
