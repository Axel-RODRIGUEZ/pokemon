from src.battle import Battle
from src.user import User
import pygame

class Menu:
    
    def __init__(self, buttons: dict, user: User):
        self.buttons = buttons
        self.user = user
    
    def run(self,screen,clock,fonts):
        background = pygame.Surface((screen.get_width(),screen.get_height()))
        background.fill(pygame.Color("#8CD3FF"))

        is_running = True

        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False

            screen.blit(background, (0, 0))

            pygame.display.update()
    
    def call_button_action(self):
        #Si bouton "Lancer une partie" -> self.__run_battle_mode()
        #Si bouton "Ajouter un Pokémon" -> self.__run_add_pokemon()
        #Si bouton "Accéder à son Pokedex" -> self.__run_pokedex()
        #Si Exit game -> __exit_game
        pass

    def __run_battle_mode(self):
        battle = Battle(self.user)

    def __run_add_pokemon_mode(self):
        pass

    def __run_pokedex_mode(self):
        pass

    def __exit_game(self):
        pass