class Pokemon:
    def __init__(self, 
                 name : str, 
                 max_hp: int, 
                 attack: int, 
                 defense: int,
                 speed: int,
                 types : dict,
                 evolution: dict,
                 sprite : dict,
                 max_stats = None, 
                 xp = 0, 
                 level = 1, 
                 is_main = False):
        
        self.name = name
        self.__max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.types = types
        self.__evolution = evolution
        self.sprite = sprite
        self.__max_stats = max_stats
        self.xp = xp
        self.__level = level
        self.is_main = is_main
        self.__xp_levels_cub = [0]
        for n in range(1, 100):
            self.__xp_levels_cub.append(int(n ** 3))
    
    def check_xp(self):
        for n in range(self.__level, 100):
            if self.xp > self.__xp_levels_cub[n-1]:
                self.__level_up()

    def __level_up(self): 
        self.__level += 1
        self.__increase_hp()
        self.__increase_atk()
        self.__increase_def()
        self.__increase_speed()
        self.__evolve()
        return None
    
    def __increase_hp(self):
        self.hp += 1
        return None

    def __increase_atk(self):
        if self.__level % 2 == 0:
            self.attack += 2
        return None
    def __increase_def(self):
        if self.__level % 2 != 0:
            self.defense += 2
        return None
    def __increase_speed(self):
        self.speed += 1
        return None
    
    def get_max_hp(self):
        return self.__max_hp

    def __evolve(self):
        if not self.__evolution:
            return None
         
        evo_level = self.__evolution["next"][0]["condition"]
        evo_name = self.__evolution["next"][0]["name"]

        if evo_level and evo_name and self.__level >= evo_level:
            self.name = evo_name
            self.hp = self.__max_stats('hp')
