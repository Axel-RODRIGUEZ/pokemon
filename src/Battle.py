from os import path, pardir
from random import randint
from pygame import image, Surface,font,event,mouse,MOUSEBUTTONDOWN,QUIT
if __name__ == "__main__":
    from DisplayBattle import DisplayBattle
    from Pokemon import Pokemon
    from User import User
    from DataManagement import DataManagement
    from Ui import Ui
    from Button import Button
else:
    from src.DisplayBattle import DisplayBattle
    from src.Pokemon import Pokemon
    from src.User import User
    from src.DataManagement import DataManagement
    from src.Ui import Ui
    from src.Button import Button
from random import random



class Battle(Ui):
    def __init__(self, screen: Surface, buttons: Button, fonts: tuple[font.Font,font.Font], user:User):
        Ui.__init__(self, screen, buttons, fonts)
        self.__turn = 0
        self.__data = DataManagement()
        self.__user = user
        self.__fighting_pokemon = self.__change_pokemon(user.main)
        self.__wild_pokemon = self.__choose_random_pokemon()
        self.__weakness_ratios = self.get_weakness_ratios()
            
    def get_weakness_ratios(self):
        self.__weakness_ratios = []
        type_data = self.__data.load_weakness_ratios()

        types_dict = {k.lower(): v for k, v in type_data.items()}

        user_ratios = {}
        for t in self.__fighting_pokemon.get_types():
            original_name = t["name"]           
            search_name = original_name.lower() 
            
            data = types_dict.get(search_name)
            user_ratios[original_name] = data
        
        wild_ratios = {}
        for t in self.__wild_pokemon.get_types():
                original_name = t["name"]
                search_name = original_name.lower()
                
                data = types_dict.get(search_name)
                wild_ratios[original_name] = data

        return user_ratios, wild_ratios

    def __change_pokemon(self, name):
        for pokemon in self.__user.pokedex:

            if pokemon["name"]["fr"] == name:
                return Pokemon(
                            name=pokemon["name"]["fr"],
                            max_hp=pokemon["stats"]["hp"],
                            attack=pokemon["stats"]["atk"],
                            defense=pokemon["stats"]["def"],
                            speed=pokemon["stats"]["vit"],
                            types=pokemon["types"],
                        )

    def __choose_random_pokemon(self):
        random = randint(0, 150)
        
        data = self.__data.load_pokemons()
        
        pkm = data[random] 
        level = randint((self.__fighting_pokemon.get_level() - 5), (self.__fighting_pokemon.get_level() + 5))
        if level <= 0:
            level = 1
        wild_pkm = Pokemon(
            name=pkm["name"]["fr"],
            max_hp=pkm["stats"]["hp"]+level,
            attack=pkm["stats"]["atk"]/3+(level*2),
            defense=pkm["stats"]["def"]+(level*2),
            speed=pkm["stats"]["vit"]+level,
            types=pkm["types"],
            level=level
        )
        
        return wild_pkm


    def __check_turn(self):
        if self.__turn == 0:
            if self.__fighting_pokemon.speed > self.__wild_pokemon.speed:
                self.__turn = self.__fighting_pokemon
            elif self.__fighting_pokemon.speed < self.__wild_pokemon.speed:
                self.__turn = self.__wild_pokemon
            else:
                self.__turn = self.__fighting_pokemon if randint(1, 2) == 1 else self.__wild_pokemon
        else:
            self.__turn = self.__wild_pokemon if self.__turn == self.__fighting_pokemon else self.__fighting_pokemon


    def __assign_attack_multi(self):
        ratios_user, ratios_wild = self.__weakness_ratios

        if isinstance(ratios_user, list):
            ratios_user = ratios_user[0]
        if isinstance(ratios_wild, list):
            ratios_wild = ratios_wild[0]

        if self.__turn == self.__fighting_pokemon:
            attacker = self.__fighting_pokemon
            defender_list = ratios_wild 
        else:
            attacker = self.__wild_pokemon
            defender_list = ratios_user

        total_bonus = 0

        for t in attacker.get_types():
            atk_type_name = t["name"].lower() 
            
            current_type_score = 1
            
            for def_name, def_data in defender_list.items():
                if def_data != None:
                    coeff = def_data.get(atk_type_name, 1)
                    current_type_score *= coeff
        
            total_bonus += current_type_score

        return total_bonus
    
    def __miss_prob(self, attacker, defender):
        prob = random()
        miss_prob_base = 0.15 - (attacker.get_level() / 1000)

        speed_ratio = attacker.speed / defender.speed
        miss_prob = miss_prob_base / speed_ratio
        miss_prob = min(miss_prob, 0.4)

        if miss_prob > prob:
            return True
        else: 
            return False

    def __attack(self):
        attack_multi = self.__assign_attack_multi()
        prob_user = self.__miss_prob(self.__fighting_pokemon, self.__wild_pokemon)
        prob_wild = self.__miss_prob(self.__wild_pokemon, self.__fighting_pokemon)

        if self.__turn == self.__fighting_pokemon:
            if prob_user:
                print("Le pokémon a raté son attaque !")
                return True
            else: 
                attack = (self.__fighting_pokemon.attack * attack_multi) - (self.__wild_pokemon.defense / 3)
                if attack < 0:
                    attack = 0

                self.__wild_pokemon.hp -= int(attack)

                return self.__check_hp(self.__wild_pokemon)
        else:

            if prob_wild:
                print("Le pokémon a raté son attaque !")
                return True
            else:
                attack = (self.__wild_pokemon.attack * attack_multi) - (self.__fighting_pokemon.defense * 30)
                if attack < 0:
                    attack = 0
                self.__fighting_pokemon.hp -= int(attack)

                pkm_alive = self.__check_hp(self.__fighting_pokemon)
                if pkm_alive == False:
                    print("Le joueur a perdu !")
                    return False
                else:
                    return True

    def __check_pokedex(self):
        check = True

        for pokemon_in_pokedex in self.__user.pokedex:
            if pokemon_in_pokedex["ko"] == True:
                check = False

            else:
                check = True
                self.__change_pokemon(None) # need function that let the user choose a pokemon in his pokedex and return his name
                break

        return check
    
    def __check_hp(self, pokemon:Pokemon):
        if pokemon.hp <= 0:
            pokemon.ko = True

        else:
            return True
        
        if pokemon == self.__fighting_pokemon and pokemon.ko:
            print(f"Le pokémon {pokemon.get_name()} est ko")

            check = self.__check_pokedex()
            return check
        
        elif pokemon == self.__wild_pokemon:
            if self.__wild_pokemon.hp <= 0:
                    print("Le pokémon sauvage est mort !")
                    self.__user.update_pokemon(self.__fighting_pokemon)
                    self.__fighting_pokemon.check_xp()
                    pokemon_to_capture = self.__compare_wild_pokemon_with_pokemon_in_pokedex()
                    self.__user.capture_pokemon(pokemon_to_capture)
                    self.__user.save_pokedex()
                    return False
            else: 
                return True
    
    def __compare_wild_pokemon_with_pokemon_in_pokedex(self):
        for pokemon in self.__user.pokedex:
            if self.__wild_pokemon.get_name() == pokemon["name"]["fr"]:
                if self.__wild_pokemon.get_level() > pokemon["stats"]["level"]:
                    return self.__wild_pokemon.pokemon_to_json()
                else: 
                    return pokemon
            else:
                return self.__wild_pokemon.pokemon_to_json()
                
        
    def __run_away(self):
        run_prob = self.__fighting_pokemon.get_level() / (self.__fighting_pokemon.get_level() + self.__wild_pokemon.get_level())
        prob = random()

        if run_prob >= prob:
            print("You have sucessfully run away !")
            return True
        else:
            print("You tried to run away but the wild pokemon stopped you !")
            return False
 
    def run(self):
        is_running = True
        successful_run_away = False
        check = True
        
        user_sprite = self.__fighting_pokemon.get_sprites()["back"]
        wild_sprite = self.__wild_pokemon.get_sprites()["front"]

        battle_display = DisplayBattle(self._screen, self._fonts, user_sprite, wild_sprite, self.__fighting_pokemon, self.__wild_pokemon)
        while is_running:
            for current_event in event.get():
                for button in self._buttons:
                    if button.rect.collidepoint(mouse.get_pos()):
                        if current_event.type == MOUSEBUTTONDOWN:
                            match button.get_target_name():
                                case "attack":
                                    self.__check_turn()
                                    check = self.__attack()
                                case "run_away":
                                    successful_run_away = self.__run_away()
                                case "pokemons":
                                    is_running = self.__run_pokedex_mode()
                        button.hovered()
                    else:
                        button.avoided()
            
                if current_event.type == QUIT:
                    is_running = False
                    
            if successful_run_away:
                break

            if check != True:
                break

            battle_display.update(self._buttons)
        return is_running