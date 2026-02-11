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
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.types = types
        self.evolution = evolution
        self.sprite = sprite
        self.max_stats = max_stats
        self.xp = xp
        self.level = level
        self.is_main = is_main
        self.xp_levels_cub = [0]
        for n in range(1, 100):
            self.xp_levels_cub.append(int(n ** 3))
    
    def check_xp(self):
        for n in range(self.level, 100):
            if self.xp > self.xp_levels_cub[n-1]:
                self.level_up()

    def level_up(self): 
        self.level += 1
        self.increase_hp()
        self.increase_atk()
        self.increase_def()
        self.increase_speed()
        return None
    
    def increase_hp(self):
        self.hp += 1
        return None

    def increase_atk(self):
        if self.level % 2 == 0:
            self.attack += 2
        return None
    def increase_def(self):
        if self.level % 2 != 0:
            self.defense += 2
        return None
    def increase_speed(self):
        self.speed += 1
        return None
    
    def get_max_hp(self):
        return self.max_hp

    def evolve(self):
        if not self.evolution:
            return None
         
        evo_level = self.evolution["next"][0]["condition"]
        evo_name = self.evolution["next"][0]["name"]

        if evo_level and evo_name and self.level >= evo_level:
            self.name = evo_name
            self.hp = self.max_stats('hp') 
