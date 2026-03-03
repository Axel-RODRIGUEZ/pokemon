from pygame import Surface,font,event,mouse,MOUSEBUTTONDOWN,QUIT,time, Rect,image
from os import path,pardir
from src.Ui import Ui
from src.Button import Button
from src.User import User
from src.MainMenu import MainMenu
from src.DisplayUserSelectMenu import DisplayUserSelectMenu

class UserSelectMenu(Ui):

    def __init__(self, 
                 screen: Surface, 
                 buttons: list[Button],   
                 fonts: list[font.Font, font.Font],
                 clock: time.Clock):
        Ui.__init__(self, screen, buttons, fonts, clock)
        self.__userselectmenu_display = DisplayUserSelectMenu(self._screen, self._fonts)
        self.__pokedex_list_area = Rect((0,0),(400,731))


    def run(self):

        is_running = True
        while is_running:
            for current_event in event.get():
                for button in self._buttons:
                    if button.rect.collidepoint(mouse.get_pos()):
                        button.hovered()
                    else:
                        button.avoided()
                if current_event.type == MOUSEBUTTONDOWN:
                    if self.__pokedex_list_area.collidepoint(mouse.get_pos()):
                            if current_event.button == 4: # Scroll
                                for button in self._buttons[:-1]:
                                    button.lefttop = button.lefttop[0], button.lefttop[1]+50
                                    button.rect.move_ip(0,50)

                            elif current_event.button == 5:
                                for button in self._buttons[:-1]: 
                                    button.lefttop = button.lefttop[0], button.lefttop[1]-50
                                    button.rect.move_ip(0,-50)
                    if current_event.button == 1:
                        for button in self._buttons:
                            if button.rect.collidepoint(mouse.get_pos()) and button.get_target_name() == "return":
                                return True
                            elif button.rect.collidepoint(mouse.get_pos()) and button.get_target_name() != 'return':
                                user_id = button.get_target_name()
                                is_running = self.__run_MainMenu(user_id)
                                return is_running
                elif current_event.type == QUIT:
                    is_running = False

                else:
                    pass 
                
            self.__userselectmenu_display.update(self._buttons)
        return is_running


    def __run_MainMenu(self, user_id):
            BASE_DIR = path.dirname(path.abspath(__file__))
            UI_IMAGES_PATH = path.join(BASE_DIR, pardir,"assets", "images", "ui", "menu")
            print(UI_IMAGES_PATH)
            user = User(is_new= False,id= user_id)
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
                user, 
                self._fonts,
                self._clock)
            is_running = menu.run()
            return is_running
