from pygame import Surface,Rect,font,event,mouse,MOUSEBUTTONDOWN,QUIT, time
from src.Ui import Ui
from src.DisplayPokedexMenu import DisplayPokedexMenu
from src.Button import Button
from src.User import User


class PokedexMenu(Ui):
    
    def __init__(self, 
                 screen: Surface, 
                 buttons: list[Button], 
                 user: User, 
                 fonts: list[font.Font, font.Font],
                 clock: time.Clock,
                 selection_mode: bool = False):
        
        Ui.__init__(self, screen, buttons, fonts, clock)

        self.__pokedex_menu_display = DisplayPokedexMenu(self._screen, self._fonts, selection_mode)
        self.__user = user
        self.__poke_list_area = Rect((0,0),(400,731))
        self.__selection_mode = selection_mode


    def run(self):
        
        pokemon_details = {}
        is_running = True
        if self.__selection_mode:
            number_of_button_to_ignore = 1

        else:
            number_of_button_to_ignore = 2

        while is_running:
            for current_event in event.get():
                for button in self._buttons:
                    if button.rect.collidepoint(mouse.get_pos()):
                        button.hovered()
                        for pokemon in self.__user.pokedex:
                            if str(pokemon["name"]["fr"]) == button.get_target_name():
                                pokemon_details = pokemon

                    else:
                        button.avoided()

                if self.__poke_list_area.collidepoint(mouse.get_pos()):
                    if current_event.type == MOUSEBUTTONDOWN:
                        if current_event.button == 4: # Scroll
                            for button in self._buttons[:-number_of_button_to_ignore]: #Ignore last two elements
                                button.lefttop = button.lefttop[0], button.lefttop[1]+50
                                button.rect.move_ip(0,50)

                        elif current_event.button == 5:
                            for button in self._buttons[:-number_of_button_to_ignore]: #Ignore last two elements
                                button.lefttop = button.lefttop[0], button.lefttop[1]-50
                                button.rect.move_ip(0,-50)

                        elif current_event.button == 1 and self.__selection_mode:
                            for button in self._buttons:
                                if button.rect.collidepoint(mouse.get_pos()):
                                    for pokemon in self.__user.pokedex:
                                        if button.get_target_name() == pokemon["name"]["fr"]:
                                            if pokemon["ko"] == False:
                                                return button.get_target_name()
                                            
                                            else:
                                                pass

                elif current_event.type == MOUSEBUTTONDOWN:
                    for button in self._buttons:
                        if button.rect.collidepoint(mouse.get_pos()) and button.get_target_name() == "return":
                            if self.__selection_mode:
                                return None
                            
                            else:
                                return is_running
                        elif button.rect.collidepoint(mouse.get_pos()) and button.get_target_name() == "heal":
                            for pokemon in self.__user.pokedex:
                                pokemon["stats"]["hp"] = pokemon["stats"]["max_hp"]
                                pokemon["ko"] = False
                            self.__user.save_pokedex()
                elif current_event.type == QUIT:
                    is_running = False

                else:
                    pass
                
            self.__pokedex_menu_display.update(self._buttons, pokemon_details)
        return is_running