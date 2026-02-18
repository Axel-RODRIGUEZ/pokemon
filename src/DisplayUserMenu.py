from src.Display import Display
from pygame import Surface,font,image,display, transform
from os import path,pardir

class DisplayUserMenu(Display):

    def __init__(self, screen: Surface, fonts: tuple[font.Font, font.Font]):
        Display.__init__(self, screen, fonts)
        UI_IMAGES_PATH = path.join(self._BASE_DIR, pardir, "assets", "images", "ui")
        self.__logo = image.load(path.join(UI_IMAGES_PATH, 'menu', 'logo.png'))
        #self.__dialog_box = image.load(path.join(UI_IMAGES_PATH, "dialog_box.png"))
        #self.__dialog_box = transform.scale(self.__dialog_box,(800,170))
        start_background = image.load(path.join(UI_IMAGES_PATH, "background-plaine.png"))
        self._background = transform.scale(start_background,(self._screen.get_width(),self._screen.get_height()))


    def update(self, buttons: list = []):
        self._screen.blit(self._background, (0, 0))
        self._screen.blit(self.__logo, (self.__logo.get_rect(center = self._background.get_rect().center)))
        if len(buttons) > 0:
            for button in buttons:
                self._draw_button(button)
        display.update()