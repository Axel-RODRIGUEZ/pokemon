class Pokemon:
    def __init__(self, name, max_hp, attack, defense, speed, types, xp = 0, sprite = 0 , level = 1):
        self.name = name
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.level = level
        self.sprite = sprite
        self.types = types
        self.xp = xp
        self.xp_levels_cub = [0]
        for n in range(1, 100):
            self.xp_levels_cub.append(int(n ** 3))
    
    def check_xp(self):
        for n in range(self.level, 100):
            if self.xp > self.xp_levels_cub[n-1]:
                self.level_up()

    def level_up(self): 
        self.level += 1

        return None
    
    def evolve(self):
         
        return None

