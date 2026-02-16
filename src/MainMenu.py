from pygame import Surface,font,event,mouse,MOUSEBUTTONDOWN,QUIT

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
                 fonts: list[font.Font, font.Font]):
        Ui.__init__(self, screen, buttons, user, fonts)
    
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
        battle = Battle(self._user)
        is_running = battle.run()
        return is_running

    def __run_add_pokemon_mode(self):
        print("Run add pokemon mode")

    def __run_pokedex_mode(self):
        buttons = []
        for i,pokemon in enumerate(self._user.pokedex):
            buttons.append(Button(str(pokemon["pokedex_id"]), (50,100+90*i), text=pokemon["name"]["fr"]))
        buttons.append(Button("return", (950,600), text="Retour"))

        pokedex = PokedexMenu(self._screen, buttons, self._user, self._fonts)
        is_running = pokedex.run()
        return is_running