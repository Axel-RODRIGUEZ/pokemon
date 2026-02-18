from src.Display import Display
from pygame import Surface,font,image,display,transform
from os import path,pardir

class DisplayBattle(Display):

    def __init__(self, screen: Surface, fonts: tuple[font.Font, font.Font], user_sprite: Surface, wild_sprite: Surface):
        Display.__init__(self, screen, fonts)
        self.__user_sprite = transform.scale_by(user_sprite,5)
        self.__wild_sprite = transform.scale_by(wild_sprite,5)
        # self.__infos_background = Surface((300, 300))
        # self.__user_max_hp = 
        # self.__wild_max_hp = 
        # self.__user_level =

        UI_IMAGES_PATH = path.join(self._BASE_DIR, pardir, "assets", "images", "ui")


    def update(self, buttons: list = []):
        self._screen.blit(self._background, (0, 0))
        self._screen.blit(self.__user_sprite, (50, 500))
        self._screen.blit(self.__wild_sprite, (850, 0))
        if len(buttons) > 0:
            for button in buttons:
                self._draw_button(button)
        display.update()