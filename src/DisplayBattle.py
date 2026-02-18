from src.Display import Display
from pygame import Surface,font,image,display
from os import path,pardir

class DisplayBattle(Display):

    def __init__(self, screen: Surface, fonts: tuple[font.Font, font.Font]):
        Display.__init__(self, screen, fonts)
        UI_IMAGES_PATH = path.join(self._BASE_DIR, pardir, "assets", "images", "ui")

    def update(self, buttons: list = []):
        self._screen.blit(self._background, (0, 0))
        
        if len(buttons) > 0:
            for button in buttons:
                self._draw_button(button)
        display.update()