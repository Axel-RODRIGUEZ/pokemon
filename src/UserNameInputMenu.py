from pygame import Surface,font,event,mouse,MOUSEBUTTONDOWN,QUIT,time,mixer,KEYDOWN,K_BACKSPACE, K_RETURN,draw

from src.Ui import Ui
from src.StarterMenu import StarterMenu
from src.Button import Button
from src.User import User
from src.DisplayUserNameInputMenu import DisplayUserNameInputMenu

class UserNameInputMenu(Ui):

    def __init__(self, 
                 screen: Surface, 
                 buttons: list[Button],   
                 fonts: list[font.Font, font.Font],
                 clock: time.Clock):
        Ui.__init__(self, screen, buttons, fonts, clock)
        self.__usernameinputmenu_display = DisplayUserNameInputMenu(self._screen, self._fonts)  
    
    def __run_StarterMenu(self, typed_text):
        WHITE = (255,255,255)
        BLACK = (0,0,0)
        PURPLE = (200, 50, 50)
        user = User(is_new= True,name_input= typed_text)

        starter_menu = StarterMenu(self._screen,
                                   [Button("Pokemon 1",(150,215),(300,300), text = "Pokemon 1", color = WHITE,font_color= BLACK), 
                                    Button("Pokemon 2",(500,215),(300,300), text = "Pokemon 2",color = BLACK),
                                    Button("Pokemon 3",(850,215),(300,300),text = "Pokemon 3",color = PURPLE),
                                    Button("Quit",(850,215),(250,70),text = "Retour",color = PURPLE)],
                                    user,
                                    self._fonts,
                                    self._clock
                                    )
        starter_menu.run()


    def run(self):
        is_running = True
        typed_text = ""
        while is_running:
            for current_event in event.get():
                for button in self._buttons:
                    if button.rect.collidepoint(mouse.get_pos()):
                        button.hovered()
                    else:
                        button.avoided()
                    
                if current_event.type == KEYDOWN:
                    if current_event.key == K_BACKSPACE:
                        typed_text = typed_text[:-1]
                    elif current_event.key == K_RETURN:
                        if typed_text.strip():
                            return ("confirm", typed_text.strip())
                    else:
                        if len(typed_text) < 20:
                            typed_text += current_event.unicode

                elif current_event.type == MOUSEBUTTONDOWN:
                    for button in self._buttons:
                        if button.rect.collidepoint(mouse.get_pos()):
                            match button.get_target_name():
                                case "Confirm":
                                    is_running = self.__run_StarterMenu(typed_text)
                                case "Cancel":
                                    return True

                elif current_event.type == QUIT:
                    is_running = False

                else:
                    pass

            self.__usernameinputmenu_display.update(typed_text,self._buttons)