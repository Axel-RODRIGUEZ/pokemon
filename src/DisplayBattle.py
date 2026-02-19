from src.Display import Display
from src.User import User
from src.Pokemon import Pokemon
from pygame import Surface,font,image,display,transform, draw
from os import path,pardir

class DisplayBattle(Display):

    def __init__(self, screen: Surface, fonts: tuple[font.Font, font.Font], user_sprite: Surface, wild_sprite: Surface, fighting_pokemon: Pokemon, wild_pokemon: Pokemon):
        Display.__init__(self, screen, fonts)
        self.__fighting_pokemon = fighting_pokemon
        self.__wild_pokemon = wild_pokemon
        self.__user_sprite = transform.scale_by(user_sprite,5)
        self.__wild_sprite = transform.scale_by(wild_sprite,5)
        self.__infos_background_border = Surface((310, 110))
        self.__infos_background = Surface((300, 100))
        # self.__user_level_bar = 
        # self.__user_max_hp_bar = 
        # self.__wild_max_hp_bar =
        # self.__user_hp_bar = 
        # self.__wild_hp_bar = 
        # self.__user_xp_bar = 
        

        UI_IMAGES_PATH = path.join(self._BASE_DIR, pardir, "assets", "images", "ui")

    def draw_text(self,text, color, center, window_surface):
        fonts = self._fonts[2]
        text_surface = fonts.render(text, True, color)
        text_rect = text_surface.get_rect(center = center)
        window_surface.blit(text_surface, text_rect)

    def update(self, buttons: list = []):
        self._screen.blit(self._background, (0, 0))
        self._screen.blit(self.__user_sprite, (50, 500))
        self._screen.blit(self.__wild_sprite, (850, 0))

        # USER 
        ratio_user = self.__fighting_pokemon.hp / self.__fighting_pokemon.get_max_hp()

        self.__infos_background_border.fill((0, 0, 0))
        self._screen.blit(self.__infos_background_border, (345, 595))
        self.__infos_background.fill((255, 255, 255))
        self._screen.blit(self.__infos_background, (350, 600))

        self.draw_text(f"Niveau {self.__fighting_pokemon.get_level()}", (0,0,0), (400,620) ,self._screen) #Changer niveau
        self.draw_text(self.__fighting_pokemon.get_name(), (0,0,0), (420,640), self._screen)

        draw.rect(self._screen, "black", (370, 660, 210, 30))
        draw.rect(self._screen, "green", (375, 665, 200 * ratio_user, 20))

        # WILD
        ratio_wild = self.__wild_pokemon.hp / self.__wild_pokemon.get_max_hp()
        self.__infos_background_border.fill((0, 0, 0))
        self._screen.blit(self.__infos_background_border, (545, 95))
        self.__infos_background.fill((255, 255, 255))
        self._screen.blit(self.__infos_background, (550, 100))

        self.draw_text(f"Niveau {self.__wild_pokemon.get_level()}", (0,0,0), (800,120) ,self._screen)
        self.draw_text(self.__wild_pokemon.get_name(), (0,0,0), (770,140) ,self._screen)

        draw.rect(self._screen, "black", (620, 160, 210, 30))
        draw.rect(self._screen, "green", (625, 165, 200 * ratio_wild, 20))
        
                
        if len(buttons) > 0:
            for button in buttons:
                self._draw_button(button)
        display.update()