from pygame import Surface,time,font
from src.button import Button

class Display:
    def __init__(self, 
                 screen: Surface, 
                 clock: time.Clock, 
                 fonts: tuple[font.Font, font.Font]):
        self.__screen = screen
        self.__clock = clock
        self.__fonts = fonts

    def display_menu(self, buttons: dict):
        pass

    def display_battle(self, buttons: dict):
        pass

    def _draw_button(self, button: Button):
        surface = Surface((button.rect.w,button.rect.h))
        surface.fill(button.current_color)
        if button.text != "":
            text_surf = self.__fonts[0].render(button.text, True, button.current_font_color)
            surface.blit(text_surf, text_surf.get_rect(center = surface.get_rect().center))
        self.__screen.blit(surface, button.rect.x, button.rect.y)