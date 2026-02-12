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
                 level = 1
                 ):
        
        self.name = name
        self.__max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.types = types
        self.__evolution = evolution # how to get this in level_up?
        self.sprite = sprite
        self.__max_stats = max_stats # how we check this point in battle?
        self.xp = xp
        self.__level = level
        self.ko = False
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
        if self.hp + 1 < self.__max_stats:
            self.hp += 1
        return None

    def __increase_atk(self):
        if self.__level % 2 == 0 and self.attack  + 2 < self.__max_stats:
            self.attack += 2
        return None
    def __increase_def(self):
        if self.__level % 2 != 0 and self.defense  + 2 < self.__max_stats:
            self.defense += 2
        return None
    def __increase_speed(self):
        if self.speed + 1 < self.__max_stats:
            self.speed += 1
        return None
    
    def get_max_hp(self):
        return self.__max_hp
    
    def get_level(self):
        return self.__level

    def __evolve(self):
        if not self.__evolution:
            return None
         
        evo_level = self.__evolution["next"][0]["condition"]
        evo_id = self.__evolution["next"][0]["pokedex_id"]

        if evo_level and evo_id and self.__level >= evo_level:
            self.name = evo_id
            self.hp = self.__max_stats('hp')
            self.attack = self.__max_stats('atk')
            self.defense = self.__max_stats('def')
            self.speed = self.__max_stats('vit')
