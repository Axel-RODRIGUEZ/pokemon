from src.Display import Display
from pygame import Surface,font,image,display,transform,draw
from os import path,pardir

class DisplayUserNameInputMenu(Display):

    def __init__(self, screen: Surface, fonts: tuple[font.Font, font.Font]):
        Display.__init__(self, screen, fonts)
        
        UI_IMAGES_PATH = path.join(self._BASE_DIR, pardir, "assets", "images", "ui")
        self.__logo = image.load(path.join(UI_IMAGES_PATH, 'menu', 'logo.png'))
        self._background = transform.scale(image.load(path.join(UI_IMAGES_PATH, "main_background.png")),(self._screen.get_width(),self._screen.get_height()))
        self.__dialog_box = image.load(path.join(UI_IMAGES_PATH, "dialog_box.png"))
        self.__dialog_box = transform.scale(self.__dialog_box,(800,170))
    def draw_text(self,text, color, center, window_surface):
        fonts = self._fonts[1]
        text_surface = fonts.render(text, True, color)
        text_rect = text_surface.get_rect(center = center)
        window_surface.blit(text_surface, text_rect)

    def update(self, typed_text, buttons: list = []):
        GRAY = (200, 200, 200)
        self._screen.blit(self._background, (0, 0))
        self._screen.blit(self.__logo, (self.__logo.get_rect(center = self._background.get_rect().center)))
        draw.rect(self._screen, GRAY, (self._screen.get_width() //2 - 200, self._screen.get_height() // 2+70,400,60))
        self._screen.blit(self.__dialog_box,(250,-10))
        self.draw_text("Choisi ton Pseudo", (0,0,0), (650,70) ,self._screen)
        text_surface = self._fonts[0].render(typed_text, True, (0,0,0))
        text_rect = text_surface.get_rect(center=(self._screen.get_width() // 2, self._screen.get_height() // 2 + 100))
        self._screen.blit(text_surface,text_rect)
        if len(buttons) > 0:
            for button in buttons:
                self._draw_button(button)
        display.update()