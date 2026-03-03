from pygame import Surface,font,event,mouse,MOUSEBUTTONDOWN,QUIT,time,mixer,KEYDOWN,K_BACKSPACE, K_RETURN

from src.Ui import Ui
from src.DisplayUserMenu import DisplayUserMenu
from src.DataManagement import DataManagement
from src.UserSelectMenu import UserSelectMenu
from src.UserNameInputMenu import UserNameInputMenu

from src.Button import Button
from src.User import User

class UserMenu(Ui):

    def __init__(self, 
                 screen: Surface, 
                 buttons: list[Button],   
                 fonts: list[font.Font, font.Font],
                 clock: time.Clock):
        Ui.__init__(self, screen, buttons, fonts, clock)
        self.__data_management = DataManagement()
        self.__users_pokedex = self.__data_management.read_pokedexs_json()


    def __run_UserSelectMenu(self):
        buttons = []
        for user_id in self.__users_pokedex:
            buttons.append(Button(target_name = str(user_id), lefttop= (50,100+90*int(user_id)), text=self.__users_pokedex[user_id]["name"]))
        buttons.append(Button("return", (957,607), text="Retour"))

        users_pokedex = UserSelectMenu(self._screen, buttons, self._fonts, self._clock)
        is_running = users_pokedex.run()
        return is_running

    def __run_UserNameInputMenu(self):
        WHITE = (255,255,255)
        BLACK = (0,0,0)
        PURPLE = (200, 50, 50)
        username_menu = UserNameInputMenu(self._screen,
                            [Button("Confirm",(300,607), text = "Confirmer", color = WHITE,font_color= BLACK), 
                            Button("Cancel",(700,607), text = "Annuler",color = BLACK)],
                            self._fonts,
                            self._clock
                            )
        username_menu.run()
        return True
        
    def run(self):
        mixer.music.play(-1)
        UserMenu_display = DisplayUserMenu(self._screen,self._fonts)
        is_running = True
        while is_running:
            for current_event in event.get():
                for button in self._buttons:
                    if button.rect.collidepoint(mouse.get_pos()):
                        if current_event.type == MOUSEBUTTONDOWN:
                            match button.get_target_name():
                                case "New Player":
                                    is_running = self.__run_UserNameInputMenu()
                                    #is_running = self.__run_StarterMenu()
                                case "Load save":
                                    is_running = self.__run_UserSelectMenu()
                                case "Quit":
                                    is_running = False
                        button.hovered()
                    else:
                        button.avoided()
                if current_event.type == QUIT:
                    is_running = False
            UserMenu_display.update(self._buttons)