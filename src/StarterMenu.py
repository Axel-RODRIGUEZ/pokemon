from pygame import Surface,font,event,mouse,MOUSEBUTTONDOWN,QUIT

from src.Ui import Ui
from src.DisplayStarterMenu import DisplayStarterMenu
from src.DataManagement import DataManagement
#from src.Pokemon import pokemon_to_on

from src.Button import Button
from src.User import User
from src.MainMenu import MainMenu

class StarterMenu(Ui):

    def __init__(self, 
                 screen: Surface, 
                 buttons: list[Button], 
                 user: User, 
                 fonts: list[font.Font, font.Font]):
        Ui.__init__(self, screen, buttons, user, fonts)
        self.__data_manager = DataManagement()

    def starter_load(self):
        starters = []
        starters.append(self.__data_manager.load_pokemon_by_id(1))
        starters.append(self.__data_manager.load_pokemon_by_id(4))
        starters.append(self.__data_manager.load_pokemon_by_id(7))
        for id in starters:
            starters[id]['is_main']
        return starters

    def starter_save(self):
        self.__data_manager.save_pokedex()

    def run(self):
        datas = DataManagement()
        datas.load_pokedexs 
        user_id = self._user.get_save_id()
        starter_display = DisplayStarterMenu(self._screen,self._fonts)
        is_running = True
        while is_running:
            for current_even in event.get():
                for button in self._buttons:
                    if button.rect.collidepoint(mouse.get_pos()):
                        if current_even.type == MOUSEBUTTONDOWN:
                            match button.get_target_name():
                                case "Pokemon 1":
                                    self._user.pokedex
                                    #self._user.pokedex.append(self.starter_load()[0])
                                    #self._user.pokedex["pokedex"].append()
                                    is_running = self.__run_MainMenu()
                                case "Pokemon 2":
                                    self._user.pokedex.append(self.starter_load()[1])
                                    is_running = self.__run_MainMenu()
                                case "Pokemon 3":
                                    self._user.pokedex.append(self.starter_load()[2])
                                    is_running = self.__run_MainMenu()
                if current_even.type == QUIT:
                    is_running = False
            starter_display.update(self._buttons)

    def __run_MainMenu(self):
        data = self.starter_load()
        print(data)


        menu = MainMenu(self._screen, 
                    [Button("battle", (500,450), text="Lancer une partie"),
                    Button("add_pokemon", (500,550), text="Ajouter un Pokémon"),
                    Button("pokedex", (500,650), text="Accéder au Pokédex")], 
                    self._user, 
                    self._fonts)
        is_running = menu.run()
        return is_running

