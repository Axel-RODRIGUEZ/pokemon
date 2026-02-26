from pygame import Surface,font,event,mouse,MOUSEBUTTONDOWN,QUIT,time,mixer

from src.Ui import Ui
from src.StarterMenu import StarterMenu
from src.DisplayUserMenu import DisplayUserMenu

from src.Button import Button
from src.User import User

class UserMenu(Ui):

    def __init__(self, 
                 screen: Surface, 
                 buttons: list[Button],   
                 fonts: list[font.Font, font.Font],
                 clock: time.Clock):
        Ui.__init__(self, screen, buttons, fonts, clock)

    def __run_StarterMenu(self):
        WHITE = (255,255,255)
        BLACK = (0,0,0)
        PURPLE = (200, 50, 50)
        user = User(is_new= True,name_input= "Toto")

        starter_menu = StarterMenu(self._screen,
                                   [Button("Pokemon 1",(150,215),(300,300), text = "Pokemon 1", color = WHITE,font_color= BLACK), 
                                    Button("Pokemon 2",(500,215),(300,300), text = "Pokemon 2",color = BLACK),
                                    Button("Pokemon 3",(850,215),(300,300),text = "Pokemon 3",color = PURPLE)],
                                    user,
                                    self._fonts,
                                    self._clock
                                    )
        starter_menu.run()

    def __runUserSelectMenu():
        pass


    def run(self):
        mixer.music.play()
        UserMenu_display = DisplayUserMenu(self._screen,self._fonts)
        is_running = True
        while is_running:
            for current_even in event.get():
                for button in self._buttons:
                    if button.rect.collidepoint(mouse.get_pos()):
                        if current_even.type == MOUSEBUTTONDOWN:
                            match button.get_target_name():
                                case "New Player":
                                     is_running = self.__run_StarterMenu()
                                case "Load Save":
                                    pass
                                    #is_running = self.__run_UserSelectMenu()
                                case "Quit":
                                    is_running = False
                        button.hovered()
                    else:
                        button.avoided()
                if current_even.type == QUIT:
                    is_running = False
            UserMenu_display.update(self._buttons)