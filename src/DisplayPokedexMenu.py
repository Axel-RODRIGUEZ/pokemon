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
            poketypes = poketalents = ""
            for poketype in pokemon_details["types"]: 
                poketypes += f"{poketype["name"]} / "
            for poketalent in pokemon_details["talents"]:
                poketalents += f"{poketalent["name"]} / "
            text_to_draw = f"""{pokemon_details["name"]["fr"]}
Catégorie: {pokemon_details["category"]}
Types: {poketypes[:-3]}
Talents: {poketalents[:-3]}
hp: {pokemon_details["stats"]["hp"]}
atk: {pokemon_details["stats"]["atk"]}
def: {pokemon_details["stats"]["def"]}
spe_atk: {pokemon_details["stats"]["spe_atk"]}
spe_def: {pokemon_details["stats"]["spe_def"]}
vit: {pokemon_details["stats"]["vit"]}
"""
            self._draw_multi_line_text(text_to_draw, 500, 100, 40)
            
        if len(buttons) > 0:
            for button in buttons:
                self._draw_button(button)
        display.update()