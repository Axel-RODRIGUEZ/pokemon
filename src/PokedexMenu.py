from pygame import Surface,Rect,font,event,mouse,MOUSEBUTTONDOWN,QUIT

from src.Ui import Ui
from src.DisplayPokedexMenu import DisplayPokedexMenu

from src.Button import Button
from src.User import User

class PokedexMenu(Ui):
    
    def __init__(self, 
                 screen: Surface, 
                 buttons: list[Button], 
                 user: User, 
                 fonts: list[font.Font, font.Font]):
        Ui.__init__(self, screen, buttons, user, fonts)
        self.__poke_list_rect = Rect((0,0),(400,731))

    def run(self):
        pokedex_menu_display = DisplayPokedexMenu(self._screen, self._fonts)
        is_running = True
        while is_running:
            for current_event in event.get():
                for button in self._buttons:
                    if button.rect.collidepoint(mouse.get_pos()):
                        button.hovered()
                    else:
                        button.avoided()
                if self.__poke_list_rect.collidepoint(mouse.get_pos()):
                    if current_event.type == MOUSEBUTTONDOWN:
                        # Scroll
                        if current_event.button == 4:
                            #scroll_offset = max(0, scroll_offset - 1)
                            print("+++")
                        elif current_event.button == 5:
                            #scroll_offset = min(max_scroll, scroll_offset + 1)
                            print("---")
                        else:
                            for button in self._buttons:
                                if button.rect.collidepoint(mouse.get_pos()):
                                    return button.get_target_name()
                elif current_event.type == MOUSEBUTTONDOWN:
                    for button in self._buttons:
                        if button.rect.collidepoint(mouse.get_pos()) and button.get_target_name() == "return":
                            return is_running
                
                elif current_event.type == QUIT:
                    is_running = False

            pokedex_menu_display.update(self._buttons)
        return is_running