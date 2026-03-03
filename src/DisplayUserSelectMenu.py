from src.Display import Display
from pygame import Surface,font,image,display,transform
from os import path,pardir

class DisplayUserSelectMenu(Display):

    def __init__(self, screen: Surface, fonts: tuple[font.Font, font.Font]):
        Display.__init__(self, screen, fonts)
        UI_IMAGES_PATH = path.join(self._BASE_DIR, pardir, "assets", "images", "ui")
        self.__logo = image.load(path.join(UI_IMAGES_PATH, 'menu', 'logo.png'))
        self._background = transform.scale(image.load(path.join(UI_IMAGES_PATH, "main_background.png")),(self._screen.get_width(),self._screen.get_height()))



    def update(self, buttons: list = []):
        self._screen.blit(self._background, (0, 0))
        self._screen.blit(self.__logo, (self.__logo.get_rect(center = self._background.get_rect().center)))
        
        if len(buttons) > 0:
            for button in buttons:
                self._draw_button(button)
        display.update()