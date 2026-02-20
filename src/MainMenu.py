from pygame import Surface,font,event,mouse,MOUSEBUTTONDOWN,QUIT, time

from src.Ui import Ui
from src.DisplayMainMenu import DisplayMainMenu

from src.Button import Button
from src.User import User
from src.Battle import Battle
from src.PokedexMenu import PokedexMenu

class MainMenu(Ui):
    
    def __init__(self, 
                 screen: Surface, 
                 buttons: list[Button], 
                 user: User, 
                 fonts: list[font.Font, font.Font],
                 clock: time.Clock):
        Ui.__init__(self, screen, buttons, fonts, clock)
        self.__user = user

    def run(self):
        menu_display = DisplayMainMenu(self._screen, self._fonts)
        is_running = True
        while is_running:
            for current_event in event.get():
                for button in self._buttons:
                    if button.rect.collidepoint(mouse.get_pos()):
                        if current_event.type == MOUSEBUTTONDOWN:
                            match button.get_target_name():
                                case "battle":
                                    is_running = self.__run_battle_mode()
                                case "add_pokemon":
                                    is_running = self.__run_add_pokemon_mode()
                                case "pokedex":
                                    is_running = self.__run_pokedex_mode()
                        button.hovered()
                    else:
                        button.avoided()
                
                if current_event.type == QUIT:
                    is_running = False

            menu_display.update(self._buttons)

    def __run_battle_mode(self):
        battle = Battle(self._screen, 
                        [Button("attack", (700, 590), (600, 60), text="Attaquer" ),
                         Button("run_away", (1000, 650), text="Fuir"),
                         Button("pokemons", (700, 650), text="Pokemons")
                         ], 
                         self._fonts, 
                         self.__user,
                         self._clock)
        is_running = battle.run()
        return is_running

    def __run_add_pokemon_mode(self):
        print("Run add pokemon mode")

    def __run_pokedex_mode(self):
        buttons = []
        for i,pokemon in enumerate(self.__user.pokedex):
            buttons.append(Button(str(pokemon["pokedex_id"]), (50,100+90*i), text=pokemon["name"]["fr"]))
        buttons.append(Button("return", (950,600), text="Retour"))

        pokedex = PokedexMenu(self._screen, buttons, self.__user, self._fonts, self._clock)
        is_running = pokedex.run()
        return is_running