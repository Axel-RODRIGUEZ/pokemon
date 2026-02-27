from pygame import Surface,Rect,font,event,mouse,MOUSEBUTTONDOWN,QUIT, time
from src.Ui import Ui
from src.DisplayPokemonSelectMenu import DisplayPokemonSelectMenu
from src.Button import Button
from src.User import User
from src.DataManagement import DataManagement


class PokemonSelectMenu(Ui):
    
    def __init__(self, 
                 screen: Surface, 
                 buttons: list[Button], 
                 fonts: list[font.Font, font.Font],
                 clock: time.Clock):
        
        Ui.__init__(self, screen, buttons, fonts, clock)
        self.__pokemon_select_menu_display = DisplayPokemonSelectMenu(self._screen, self._fonts)
        self.__poke_list_area = Rect((0,0),(400,731))


    def run(self):

        data_management = DataManagement()
        pokemons = data_management.read_pokemons_json()
        pokemon_details = {}
        is_running = True

        while is_running:
            for current_event in event.get():
                for button in self._buttons:
                    if button.rect.collidepoint(mouse.get_pos()):
                        button.hovered()

                        for pokemon in pokemons:
                            if str(pokemon["name"]["fr"]) == button.get_target_name():
                                pokemon_details = pokemon

                    else:
                        button.avoided()
                        for pokemon in pokemons:
                            if str(pokemon["name"]["fr"]) == button.get_target_name():
                                if pokemon["active"] == True:
                                    button.set_color((50,150,50))
                                    button.set_hovered_color((50,100,50))

                                else:
                                    button.set_color((150,50,50))
                                    button.set_hovered_color((100,50,50))
                             

                if self.__poke_list_area.collidepoint(mouse.get_pos()):
                    if current_event.type == MOUSEBUTTONDOWN:
                        if current_event.button == 4: # Scroll
                            for button in self._buttons[:-1]: #Ignore last element
                                button.lefttop = button.lefttop[0], button.lefttop[1]+50
                                button.rect.move_ip(0,50)

                        elif current_event.button == 5:
                            for button in self._buttons[:-1]: #Ignore last element
                                button.lefttop = button.lefttop[0], button.lefttop[1]-50
                                button.rect.move_ip(0,-50)

                        elif current_event.button == 1:
                            for button in self._buttons:
                                if button.rect.collidepoint(mouse.get_pos()):
                                    for pokemon in pokemons:
                                        if button.get_target_name() == pokemon["name"]["fr"]:
                                            pokemon["active"] = not pokemon["active"]

                elif current_event.type == MOUSEBUTTONDOWN:
                    for button in self._buttons:
                        if button.rect.collidepoint(mouse.get_pos()) and button.get_target_name() == "return":
                            data_management.write_pokemons_json(pokemons)
                            return is_running
                
                elif current_event.type == QUIT:
                    is_running = False

                else:
                    pass
                
            self.__pokemon_select_menu_display.update(self._buttons, pokemon_details)

        return is_running