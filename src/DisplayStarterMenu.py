from src.Display import Display
from pygame import Surface,font,image,display, transform
from os import path,pardir

class DisplayStarterMenu(Display):

    def __init__(self, screen: Surface, fonts: tuple[font.Font, font.Font]):
        Display.__init__(self, screen, fonts)
        UI_IMAGES_PATH = path.join(self._BASE_DIR, pardir, "assets", "images", "ui")
        #self.__logo = image.load(path.join(UI_IMAGES_PATH, 'menu', 'logo.png'))
        self.__dialog_box = image.load(path.join(UI_IMAGES_PATH, "dialog_box.png"))
        self.__dialog_box = transform.scale(self.__dialog_box,(800,170))
        start_background = image.load(path.join(UI_IMAGES_PATH, "starter_background.png"))
        self._background = transform.scale(start_background,(self._screen.get_width(),self._screen.get_height()))
    
    def draw_text(self,text, size, color, center, window_surface):
        fonts = self._fonts[1]
        text_surface = fonts.render(text, True, color)
        text_rect = text_surface.get_rect(center = center)
        window_surface.blit(text_surface, text_rect)
    
    def update(self, buttons: list = []):
        self._screen.blit(self._background, (0, 0))
        self._screen.blit(self.__dialog_box,(250,-10))
        self.draw_text("Choisi ton Pokemon de départ", 36, (0,0,0), (650,70) ,self._screen)
        
        if len(buttons) > 0:
            for button in buttons:
                self._draw_button(button)
        display.update()