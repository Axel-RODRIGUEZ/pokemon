from pygame import Surface,font,Color
from os import path
from src.Button import Button
from abc import ABC, abstractmethod

class Display(ABC):
    def __init__(self, 
                 screen: Surface, 
                 fonts: tuple[font.Font, font.Font]):
        self._BASE_DIR = path.dirname(path.abspath(__file__))
        self._screen = screen
        self._fonts = fonts
        self._background = Surface((screen.get_width(),screen.get_height()))
        self._background.fill(Color("#8CD3FF"))
    
    @abstractmethod
    def update(self, buttons: list[Button] = []):
        pass

    def _draw_button(self, button: Button):
        if button.get_bg_image() != None and button.get_hover_bg_image() != None:
            surface = button.current_bg_image
        else:
            surface = Surface((button.widthheight))
            surface.fill(button.current_color)

        if button.text != "":
            text_surf = self._fonts[0].render(button.text, True, button.current_font_color)
            surface.blit(text_surf, text_surf.get_rect(center = surface.get_rect().center))
        self._screen.blit(surface, button.lefttop)

    def _draw_multi_line_text(self, text: str, x: int, y: int, linegap: int, font_index: int = 0):
        lines = text.splitlines()
        for i, line in enumerate(lines):
            self._screen.blit(self._fonts[font_index].render(line, 0, (255,255,255)), (x, y + linegap*i))