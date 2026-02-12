from src.display import *

UI_IMAGES_PATH = path.join(BASE_DIR, pardir, "assets", "images", "ui")

class DisplayMainMenu(Display):

    def __init__(self, screen: Surface, fonts: tuple[font.Font, font.Font]):
        
        Display.__init__(self, screen, fonts)
        self.__logo = image.load(path.join(UI_IMAGES_PATH, 'menu', 'logo.png'))

    def display(self, buttons: list = []):
        self._screen.blit(self._background, (0, 0))
        self._screen.blit(self.__logo, (self.__logo.get_rect(center = self._background.get_rect().center)))
        
        if len(buttons) > 0:    
            for button in buttons:
                self._draw_button(button)
        display.update()