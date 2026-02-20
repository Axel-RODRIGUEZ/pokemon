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
        self.__selection_mode = selection_mode
        self.__pokedex_menu_display = DisplayPokedexMenu(self._screen, self._fonts, selection_mode)
        self.__user = user
        self.__poke_list_area = Rect((0,0),(400,731))


    def run(self):
        
        pokemon_details = {}
        is_running = True
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
                            for button in self._buttons[:-1]: #Ignore last element
                                button.lefttop = button.lefttop[0], button.lefttop[1]+50
                                button.rect.move_ip(0,50)
                        elif current_event.button == 5:
                            for button in self._buttons[:-1]: #Ignore last element
                                button.lefttop = button.lefttop[0], button.lefttop[1]-50
                                button.rect.move_ip(0,-50)
                        elif current_event.button == 1 and self.__selection_mode:
                            for button in self._buttons:
                                if button.rect.collidepoint(mouse.get_pos()):
                                    return button.get_target_name()
                elif current_event.type == MOUSEBUTTONDOWN:
                    for button in self._buttons:
                        if button.rect.collidepoint(mouse.get_pos()) and button.get_target_name() == "return":
                            if self.__selection_mode:
                                return None
                            else:
                                return is_running
                
                elif current_event.type == QUIT:
                    is_running = False

                else:
                    pass
                
            self.__pokedex_menu_display.update(self._buttons, pokemon_details)
        return is_running