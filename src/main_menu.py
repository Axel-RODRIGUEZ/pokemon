from src.battle import Battle
from src.user import User
from src.display_main_menu import *
import pygame

class MainMenu:
    
    def __init__(self, buttons: list[Button], user: User):
        self.__buttons = buttons
        self.__user = user
    
    def run(self,screen,fonts):

        menu_display = DisplayMainMenu(screen,fonts)
        is_running = True
        while is_running:
            for event in pygame.event.get():
                for button in self.__buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        if event.type == pygame.MOUSEBUTTONDOWN:
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
                
                if event.type == pygame.QUIT:
                    is_running = False

            menu_display.display(self.__buttons)

    def __run_battle_mode(self):
        battle = Battle(self.__user)
        is_running = battle.run()
        return is_running

    def __run_add_pokemon_mode(self):
        print("Run add pokemon mode")

    def __run_pokedex_mode(self):
        print("Run pokedex mode")

    def __exit_game(self):
        pass