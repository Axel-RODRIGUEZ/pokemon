from random import randint, choice
from pygame import Surface,font,event,mouse,MOUSEBUTTONDOWN,QUIT, time
if __name__ == "__main__":
    from DisplayBattle import DisplayBattle
    from Pokemon import Pokemon
    from User import User
    from DataManagement import DataManagement
    from Ui import Ui
    from Button import Button
    from PokedexMenu import PokedexMenu
else:
    from src.DisplayBattle import DisplayBattle
    from src.Pokemon import Pokemon
    from src.User import User
    from src.DataManagement import DataManagement
    from src.Ui import Ui
    from src.Button import Button
    from src.PokedexMenu import PokedexMenu
from random import random



class Battle(Ui):


    def __init__(self, screen: Surface, buttons: Button, fonts: tuple[font.Font,font.Font], user:User, clock: time.Clock):
        
        Ui.__init__(self, screen, buttons, fonts, clock)
        self.__turn = 0
        self.__data = DataManagement()
        self.__user = user
        self.__fighting_pokemon = self.__instantiate_pokemon_from_pokedex(user.main)
        self.__wild_pokemon = self.__choose_random_pokemon()
        self.__wild_attack_timer = None
        self.__weakness_ratios = self.__get_weakness_ratios()
        self.__battle_display = DisplayBattle(self._screen, self._fonts, self.__fighting_pokemon, self.__wild_pokemon, self.__turn)


    def __choose_random_pokemon(self):
        
        pokemons = self.__data.read_pokemons_json()
        active_pokemons = []

        for pokemon in pokemons:
            if pokemon["active"] == True:
                active_pokemons.append(pokemon)

        random_pokemon = choice(active_pokemons) 
        
        level = randint((self.__fighting_pokemon.get_level() - 5), (self.__fighting_pokemon.get_level() + 5))
        if level <= 0:
            level = 1
        wild_pokemon = Pokemon(
            name=random_pokemon["name"]["fr"],
            max_hp=random_pokemon["stats"]["max_hp"]+level,
            attack=random_pokemon["stats"]["atk"]/3+(level*2),
            defense=random_pokemon["stats"]["def"]+(level*2),
            speed=random_pokemon["stats"]["vit"]+level,
            types=random_pokemon["types"],
            level=level
        )
        
        return wild_pokemon    


    def __get_weakness_ratios(self):
        self.__weakness_ratios = []
        type_data = self.__data.read_weakness_ratios_json()

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


    def __check_turn(self):
        if self.__turn == 0:
            if self.__fighting_pokemon.speed > self.__wild_pokemon.speed:
                self.__turn = self.__fighting_pokemon
                self.__battle_display.turn = self.__fighting_pokemon
            elif self.__fighting_pokemon.speed < self.__wild_pokemon.speed:
                self.__turn = self.__wild_pokemon
                self.__battle_display.turn = self.__wild_pokemon
            else:
                if randint(1, 2) == 1:
                    self.__battle_display.turn = self.__fighting_pokemon
                    self.__turn = self.__fighting_pokemon
                else:
                    self.__turn = self.__wild_pokemon
                    self.__battle_display.turn = self.__wild_pokemon
        else:
            if self.__turn == self.__fighting_pokemon:
                self.__turn = self.__wild_pokemon
                self.__battle_display.turn = self.__wild_pokemon
            else:
                self.__turn = self.__fighting_pokemon
                self.__battle_display.turn = self.__fighting_pokemon


    def __is_attack_successfull(self, attacker: Pokemon, defender: Pokemon):

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
        user_attack_success = self.__is_attack_successfull(self.__fighting_pokemon, self.__wild_pokemon)
        wild_attack_success = self.__is_attack_successfull(self.__wild_pokemon, self.__fighting_pokemon)

        if self.__turn == self.__fighting_pokemon:
            if user_attack_success:
                print("Le pokémon a raté son attaque !")
                return True
            else: 
                print("Le pokémon a réussi son attaque !")
                attack = (self.__fighting_pokemon.attack * attack_multi) - (self.__wild_pokemon.defense / 3)
                if attack < 0:
                    attack = 0

                self.__wild_pokemon.hp -= int(attack)
                return False
        else:

            if wild_attack_success:
                print("Le pokémon ennemi a raté son attaque !")
                return True
            else:
                print("Le pokémon ennemi a réussi son attaque !")
                attack = (self.__wild_pokemon.attack * attack_multi) - (self.__fighting_pokemon.defense / 3)
                if attack < 0:
                    attack = 0
                self.__fighting_pokemon.hp -= int(attack)
                return False


    def __check_hp(self, pokemon_to_check:Pokemon):

        if pokemon_to_check.hp <= 0:
            pokemon_to_check.ko = True

        else:
            return True
        
        if pokemon_to_check == self.__fighting_pokemon and pokemon_to_check.ko:
            for pokemon in self.__user.pokedex:
                if pokemon_to_check.get_name() == pokemon["name"]["fr"]:
                    pokemon["ko"] = True
                    print(f"Le pokémon {pokemon_to_check.get_name()} est ko")

            team_ko = self.__check_pokemon_remaining()
            return team_ko
        
        elif pokemon_to_check == self.__wild_pokemon:
            if self.__wild_pokemon.hp <= 0:
                    print("Le pokémon sauvage est mort !")
                    self.__fighting_pokemon.increase_xp(int((self.__wild_pokemon.get_level() ** 3)/3+4))
                    self.__fighting_pokemon.check_xp()
                    self.__user.update_pokemon(self.__fighting_pokemon)
                    pokemon_to_capture = self.__best_stats_between_wild_and_user_pokemon()
                    self.__user.capture_pokemon(pokemon_to_capture)
                    self.__user.save_pokedex()
                    self.__user.update_available_pokemons()
                    return False
            
            else: 
                return True


    def __check_pokemon_remaining(self):
        pokemon_alive_remaining = True

        for pokemon_in_pokedex in self.__user.pokedex:
            if pokemon_in_pokedex["ko"] == True:
                pokemon_alive_remaining = False
            else:
                pokemon_alive_remaining = True
                self.__change_fighting_pokemon() 
                return pokemon_alive_remaining

        print("Le joueur a perdu !")
        return pokemon_alive_remaining


    def __instantiate_pokemon_from_pokedex(self, name: str):

        for pokemon in self.__user.pokedex:
            if pokemon["name"]["fr"] == name:
                return Pokemon(
                            name=pokemon["name"]["fr"],
                            max_hp=pokemon["stats"]["hp"],
                            attack=pokemon["stats"]["atk"],
                            defense=pokemon["stats"]["def"],
                            speed=pokemon["stats"]["vit"],
                            types=pokemon["types"],
                            level=pokemon["stats"]["level"],
                            xp=pokemon["stats"]["xp"] 
                        )


    def __change_fighting_pokemon(self):

        buttons = []
        for i,pokemon in enumerate(self.__user.pokedex):
            buttons.append(Button(str(pokemon["name"]["fr"]), (50,100+90*i), text=pokemon["name"]["fr"]))

        buttons.append(Button("return", (957,607), text="Retour"))
        pokedex = PokedexMenu(self._screen, buttons, self.__user, self._fonts, self._clock, True)
        new_poke_name = pokedex.run()

        if new_poke_name != None:
            self.__fighting_pokemon = self.__instantiate_pokemon_from_pokedex(new_poke_name)
            self.__battle_display.set_fighting_pokemon(self.__fighting_pokemon)
            self.__battle_display.update_fighting_pokemon_sprite()
    

    def __best_stats_between_wild_and_user_pokemon(self):

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
        animation_state = None 
        missed = None
        self.__check_turn()

        while is_running:
            
            if self.__turn == self.__fighting_pokemon:

                for current_event in event.get():
                    for button in self._buttons:
                        if button.rect.collidepoint(mouse.get_pos()):
                            if current_event.type == MOUSEBUTTONDOWN:
                                match button.get_target_name():
                                    case "attack":
                                        missed = self.__attack()
                                        check = self.__check_hp(self.__wild_pokemon)
                                        animation_state = (self.__wild_pokemon, missed)
                                        self.__check_turn()
                                    case "run_away":
                                        successful_run_away = self.__run_away()
                                    case "pokemons":
                                        self.__change_fighting_pokemon()
                             
                            button.hovered()

                        else:
                            button.avoided()

                    if current_event.type == QUIT:
                        is_running = False

            else:
                if self.__wild_attack_timer is None:
                    self.__wild_attack_timer = time.get_ticks()

                elapsed = time.get_ticks() - self.__wild_attack_timer
                if elapsed >= 2000:  
                    missed = self.__attack()
                    check = self.__check_hp(self.__fighting_pokemon)
                    animation_state = (self.__fighting_pokemon, missed)
                    self.__check_turn()
                    self.__wild_attack_timer = None
                    
            if successful_run_away:
                break

            if check != True:
                break

            if animation_state is not None:
                pokemon, missed = animation_state
                if missed:
                    done = self.__battle_display.pokemon_dodge_animation(pokemon)
                else:
                    done = self.__battle_display.pokemon_damage_animation(pokemon)
                if done:
                    animation_state = None

            self.__battle_display.update(missed, self._buttons)
            self._clock.tick(60)
        return is_running