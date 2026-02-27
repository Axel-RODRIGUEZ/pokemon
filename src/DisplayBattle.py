from src.Display import Display
from src.User import User
from src.Pokemon import Pokemon
from pygame import Surface,font,image,display,transform, draw, time
from os import path,pardir


class DisplayBattle(Display):

    def __init__(self, screen: Surface, fonts: tuple[font.Font, font.Font], fighting_pokemon: Pokemon, wild_pokemon: Pokemon, turn):

        Display.__init__(self, screen, fonts)
        
        UI_IMAGES_PATH = path.join(self._BASE_DIR, pardir, "assets", "images", "ui")
        self._background = transform.scale(image.load(path.join(UI_IMAGES_PATH, "battle_background.png")),(self._screen.get_width(),self._screen.get_height()))

        self.__fighting_pokemon = fighting_pokemon
        self.__wild_pokemon = wild_pokemon
        self.__fighting_pokemon_sprite = transform.scale_by(self.__fighting_pokemon.get_sprites()["back"],5)
        self.__wild_pokemon_sprite = transform.scale_by(self.__wild_pokemon.get_sprites()["front"],5)
        self.__infos_background_border = Surface((310, 110))
        self.__infos_background = Surface((300, 100))
        self.__pokemon_damage_time = None
        self.__wild_pokemon_sprite_xy = 850, 0
        self.__fighting_pokemon_sprite_xy = 50, 500
        
        self.turn = turn


    def __draw_text(self,text, color, center, window_surface):

        fonts = self._fonts[2]
        text_surface = fonts.render(text, True, color)
        text_rect = text_surface.get_rect(center = center)
        window_surface.blit(text_surface, text_rect)


    def set_fighting_pokemon(self, new_pokemon: Pokemon):
        self.__fighting_pokemon = new_pokemon


    def update_fighting_pokemon_sprite(self):
        self.__fighting_pokemon_sprite = transform.scale_by(self.__fighting_pokemon.get_sprites()["back"],5)


    def pokemon_damage_animation(self, pokemon: Pokemon):

        INTERVAL = 100
        DURATION = 1000
        OFFSET = 15

        if self.__pokemon_damage_time is None:
                    self.__pokemon_damage_time = time.get_ticks()
        elapsed = time.get_ticks() - self.__pokemon_damage_time

        if elapsed < DURATION:
            if (elapsed // INTERVAL) % 2 == 0:
                offset = OFFSET
            else:
                offset = -OFFSET

            if pokemon == self.__wild_pokemon:
                self.__wild_pokemon_sprite_xy = (850 + offset, 0)
            else:
                self.__fighting_pokemon_sprite_xy = (50 + offset, 500)
        else:
            self.__wild_pokemon_sprite_xy = (850, 0)
            self.__fighting_pokemon_sprite_xy = (50, 500)
            self.__pokemon_damage_time = None
            return True
        

    def pokemon_dodge_animation(self, pokemon: Pokemon):

        DURATION = 1000

        if self.__pokemon_damage_time is None:
                    self.__pokemon_damage_time = time.get_ticks()
        elapsed = time.get_ticks() - self.__pokemon_damage_time

        if elapsed < DURATION:
            if elapsed < DURATION // 2:
                offset = int((elapsed / (DURATION // 2)) * 50)   # 0 → +50px

            else:
                offset = int(((DURATION - elapsed) / (DURATION // 2)) * 50)

            if pokemon == self.__wild_pokemon:
                self.__wild_pokemon_sprite_xy = (850 + offset, 0)

            else:
                self.__fighting_pokemon_sprite_xy = (50 + offset, 500)

        else:
            self.__wild_pokemon_sprite_xy = (850, 0)
            self.__fighting_pokemon_sprite_xy = (50, 500)
            self.__pokemon_damage_time = None
            return True


    def update(self, missed, buttons: list = []):

        self._screen.blit(self._background, (0, 0))
        self._screen.blit(self.__fighting_pokemon_sprite, self.__fighting_pokemon_sprite_xy)
        self._screen.blit(self.__wild_pokemon_sprite, self.__wild_pokemon_sprite_xy)
        
        # INFO BOX
        if self.turn == 0:
            self.__draw_text(f"Calcul du tour . . .", (0,0,0), (300,300) ,self._screen)

        else:
            self.__draw_text(f"Tour actuel : {self.turn.get_name()}", (0,0,0), (300,300) ,self._screen)

        if missed:
            self.__draw_text(f" a raté son attaque !", (0,0,0), (310,310) ,self._screen)

        elif missed != True:
            self.__draw_text(f" a réussi son attaque !", (0,0,0), (310,310) ,self._screen) 

        else: 
            pass
        ###    ADD POKEMON IN THE TEXT ###
        # USER
        ratio_user = self.__fighting_pokemon.hp / self.__fighting_pokemon.get_max_hp()

        self.__infos_background_border.fill((0, 0, 0))
        self._screen.blit(self.__infos_background_border, (345, 595))
        self.__infos_background.fill((255, 255, 255))
        self._screen.blit(self.__infos_background, (350, 600))

        self.__draw_text(f"Niveau {self.__fighting_pokemon.get_level()}", (0,0,0), (400,620) ,self._screen)
        self.__draw_text(self.__fighting_pokemon.get_name(), (0,0,0), (420,640), self._screen)

        draw.rect(self._screen, "black", (370, 660, 210, 30))
        draw.rect(self._screen, "green", (375, 665, 200 * ratio_user, 20))

        # WILD
        ratio_wild = self.__wild_pokemon.hp / self.__wild_pokemon.get_max_hp()
        self.__infos_background_border.fill((0, 0, 0))
        self._screen.blit(self.__infos_background_border, (545, 95))
        self.__infos_background.fill((255, 255, 255))
        self._screen.blit(self.__infos_background, (550, 100))

        self.__draw_text(f"Niveau {self.__wild_pokemon.get_level()}", (0,0,0), (800,120) ,self._screen)
        self.__draw_text(self.__wild_pokemon.get_name(), (0,0,0), (770,140) ,self._screen)

        draw.rect(self._screen, "black", (620, 160, 210, 30))
        draw.rect(self._screen, "green", (625, 165, 200 * ratio_wild, 20))
           
        if len(buttons) > 0:
            for button in buttons:
                self._draw_button(button)

        display.update()