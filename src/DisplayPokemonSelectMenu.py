from src.Display import Display
from pygame import Surface,font,image,display,transform
from os import path,pardir

class DisplayPokemonSelectMenu(Display):

    def __init__(self, screen: Surface, fonts: tuple[font.Font, font.Font]):
        Display.__init__(self, screen, fonts)
        IMAGES_PATH = path.join(self._BASE_DIR, pardir, "assets", "images")
        #self.__logo = image.load(path.join(IMAGES_PATH, 'ui', 'menu', 'logo.png'))
        self.__SPRITES_PATH = path.join(IMAGES_PATH, "sprites")

    def update(self, buttons: list = [], pokemon_details: dict = {}):
        self._screen.blit(self._background, (0, 0))
        #self._screen.blit(self.__logo, (self.__logo.get_rect(center = self._background.get_rect().center)))
        
        self._screen.blit(self._fonts[1].render("Pokémons que tu peux rencontrer", 0, (255,255,255)), (400, 50))
        if bool(pokemon_details): #Check if pokemon_details is empty
            if pokemon_details["ko"] == True:
                ko_text = "KO"
            else:
                ko_text = ""
            poketypes = poketalents = ""
            for poketype in pokemon_details["types"]: 
                poketypes += f"{poketype["name"]} / "
            for poketalent in pokemon_details["talents"]:
                poketalents += f"{poketalent["name"]} / "
            text_to_draw = f"""{pokemon_details["name"]["fr"]} {ko_text}
Catégorie: {pokemon_details["category"]}
Types: {poketypes[:-3]}
Talents: {poketalents[:-3]}
max_hp: {pokemon_details["stats"]["max_hp"]}
atk: {pokemon_details["stats"]["atk"]}
def: {pokemon_details["stats"]["def"]}
spe_atk: {pokemon_details["stats"]["spe_atk"]}
spe_def: {pokemon_details["stats"]["spe_def"]}
vit: {pokemon_details["stats"]["vit"]}
"""
            self._draw_multi_line_text(text_to_draw, 450, 200, 40)
            self.__load_sprite(pokemon_details["pokedex_id"], pokemon_details["ko"])
            self.__blit_sprite()
            
        if len(buttons) > 0:
            for button in buttons:
                self._draw_button(button)
        display.update()

    def __load_sprite(self, pokedex_id, ko):
        if ko == True:
            sprite_path = path.join(self.__SPRITES_PATH, 'backs', f'{pokedex_id}.png')
        else:
            sprite_path = path.join(self.__SPRITES_PATH, 'fronts', f'{pokedex_id}.png')
        self.__sprite = transform.scale_by(image.load(sprite_path).convert_alpha(), 5)

    def __blit_sprite(self):
        self._screen.blit(self.__sprite,(950,50))