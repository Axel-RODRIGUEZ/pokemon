from pygame import display,Surface,time,font,Color,image
from os import path,pardir
from src.button import Button
from abc import ABC, abstractmethod

BASE_DIR = path.dirname(path.abspath(__file__))

class Display(ABC):
    def __init__(self, 
                 screen: Surface, 
                 fonts: tuple[font.Font, font.Font]):
        self._screen = screen
        self._fonts = fonts
        self._background = Surface((screen.get_width(),screen.get_height()))
        self._background.fill(Color("#8CD3FF"))
    
    @abstractmethod
    def display(self, buttons: list = []):
        pass

    def _draw_button(self, button: Button):
        surface = Surface((button.widthheight))
        surface.fill(button.current_color)
        if button.text != "":
            text_surf = self._fonts[0].render(button.text, True, button.current_font_color)
            surface.blit(text_surf, text_surf.get_rect(center = surface.get_rect().center))
        self._screen.blit(surface, button.lefttop)