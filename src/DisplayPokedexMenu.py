from src.Display import Display
from pygame import Surface,font,image,display
from os import path,pardir

class DisplayPokedexMenu(Display):

    def __init__(self, screen: Surface, fonts: tuple[font.Font, font.Font]):
        Display.__init__(self, screen, fonts)
        UI_IMAGES_PATH = path.join(self._BASE_DIR, pardir, "assets", "images", "ui")
        #self.__logo = image.load(path.join(UI_IMAGES_PATH, 'menu', 'logo.png'))

    def update(self, buttons: list = [], pokemon_details: dict = {}):
        self._screen.blit(self._background, (0, 0))
        #self._screen.blit(self.__logo, (self.__logo.get_rect(center = self._background.get_rect().center)))
        if bool(pokemon_details): #Check if pokemon_details is empty
            text_surf = self._fonts[0].render(pokemon_details["category"], True, (255,255,255))
            self._screen.blit(text_surf, text_surf.get_rect(center = self._screen.get_rect().center))
            
        if len(buttons) > 0:
            for button in buttons:
                self._draw_button(button)
        display.update()