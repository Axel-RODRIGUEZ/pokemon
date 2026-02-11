from pygame import display,Surface,time,font,Color
from src.button import Button

class Display:
    def __init__(self, 
                 screen: Surface, 
                 fonts: tuple[font.Font, font.Font]):
        self.__screen = screen
        self.__fonts = fonts
        self.__background = Surface((screen.get_width(),screen.get_height()))
        self.__background.fill(Color("#8CD3FF"))

    def display_menu(self, buttons: list = []):
        self.__screen.blit(self.__background, (0, 0))
        if len(buttons) > 0:    
            for button in buttons:
                self.__draw_button(button)
        display.update()

    def display_battle(self, buttons: dict):
        pass

    def __draw_button(self, button: Button):
        surface = Surface((button.widthheight))
        surface.fill(button.current_color)
        if button.text != "":
            text_surf = self.__fonts[0].render(button.text, True, button.current_font_color)
            surface.blit(text_surf, text_surf.get_rect(center = surface.get_rect().center))
        self.__screen.blit(surface, button.lefttop)