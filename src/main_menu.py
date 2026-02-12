from src.battle import Battle
from src.user import User
from src.display_main_menu import DisplayMainMenu
import pygame

class MainMenu:
    
    def __init__(self, buttons: list, user: User):
        self.__buttons = buttons
        self.__user = user
    
    def run(self,screen,fonts):

        menu_display = DisplayMainMenu(screen,fonts)
        is_running = True
        while is_running:
            for event in pygame.event.get():
                for button in self.__buttons:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        #pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        #pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                        button.hovered()
                    else:
                        button.avoided()
                
                if event.type == pygame.QUIT:
                    is_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.__buttons:
                        pass

            menu_display.display(self.__buttons)
    
    def call_button_action(self):
        #Si bouton "Lancer une partie" -> self.__run_battle_mode()
        #Si bouton "Ajouter un Pokémon" -> self.__run_add_pokemon()
        #Si bouton "Accéder à son Pokedex" -> self.__run_pokedex()
        #Si Exit game -> __exit_game
        pass

    def __run_battle_mode(self):
        battle = Battle(self.__user)

    def __run_add_pokemon_mode(self):
        pass

    def __run_pokedex_mode(self):
        pass

    def __exit_game(self):
        pass