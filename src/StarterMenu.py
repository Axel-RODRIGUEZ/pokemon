from pygame import Surface,font,event,mouse,MOUSEBUTTONDOWN,QUIT,image
from os import path,pardir

from src.Ui import Ui
from src.DisplayStarterMenu import DisplayStarterMenu
from src.DataManagement import DataManagement

from src.Button import Button
from src.User import User
from src.MainMenu import MainMenu

class StarterMenu(Ui):

    def __init__(self, 
                 screen: Surface, 
                 buttons: list[Button], 
                 user: User, 
                 fonts: list[font.Font, font.Font]):
        Ui.__init__(self, screen, buttons, fonts)
        self.__user = user
        self.__data_manager = DataManagement()
        self.__pokemons_data = self.__data_manager.load_pokemons()
        self.__starters = self.starter_load()

    def starter_load(self):
        starters = []
        starters.append(self.__pokemons_data[0])
        starters.append(self.__pokemons_data[3])
        starters.append(self.__pokemons_data[6])
        return starters

    def starter_save(self):
        self.__data_manager.write_pokedexs()

    def run(self):
        starter_display = DisplayStarterMenu(self._screen,self._fonts)
        is_running = True
        while is_running:
            for current_even in event.get():
                for button in self._buttons:
                    if button.rect.collidepoint(mouse.get_pos()):
                        if current_even.type == MOUSEBUTTONDOWN:
                            match button.get_target_name():
                                case "Pokemon 1":
                                    print(self.__user.pokedex)
                                    self.__user.pokedex.append(self.__starters[0])
                                case "Pokemon 2":
                                    self.__user.pokedex.append(self.__starters[1])
                                case "Pokemon 3":
                                    self.__user.pokedex.append(self.__starters[2])
                            self.__user.main = self.__user.pokedex[0]["name"]["fr"]
                            is_running = self.__run_MainMenu()
                if current_even.type == QUIT:
                    is_running = False
            starter_display.update(self._buttons)

    def __run_MainMenu(self):
        BASE_DIR = path.dirname(path.abspath(__file__))
        UI_IMAGES_PATH = path.join(BASE_DIR, pardir,"assets", "images", "ui", "menu")
        print(UI_IMAGES_PATH)
        menu = MainMenu(self._screen, 
            [Button("battle", 
                    (500,450), 
                    text="Lancer une partie", 
                    bg_image=image.load(path.join(UI_IMAGES_PATH, "button.png")), 
                    hover_bg_image=image.load(path.join(UI_IMAGES_PATH, "hover_button.png"))),
            Button("add_pokemon", 
                    (500,550), 
                    text="Ajouter un Pokémon", 
                    bg_image=image.load(path.join(UI_IMAGES_PATH, "button.png")), 
                    hover_bg_image=image.load(path.join(UI_IMAGES_PATH, "hover_button.png"))),
            Button("pokedex", 
                    (500,650), 
                    text="Accéder au Pokédex", 
                    bg_image=image.load(path.join(UI_IMAGES_PATH, "button.png")), 
                    hover_bg_image=image.load(path.join(UI_IMAGES_PATH, "hover_button.png")))], 
            self.__user, 
            self._fonts)
        is_running = menu.run()
        return is_running

