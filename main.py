import pygame
from os import path
from src.MainMenu import MainMenu
from src.StarterMenu import StarterMenu
from src.User import User
from src.Button import Button


def main():

    BASE_DIR = path.dirname(path.abspath(__file__))
    FONT_PATH = path.join(BASE_DIR, "assets", "fonts", "LiberationSans-Regular.ttf")

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Pokemon')
    
    screen = pygame.display.set_mode((1300, 731))
    clock = pygame.time.Clock()
    fonts = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50)

    user = User(is_new=False)
    #menu = MainMenu(screen, 
    #                [Button("battle", (500,450), text="Lancer une partie"),
    #                Button("add_pokemon", (500,550), text="Ajouter un Pokémon"),
    #                Button("pokedex", (500,650), text="Accéder au Pokédex")], 
    #                user, 
    #                fonts)
    #menu.run()
    
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    PURPLE = (200, 50, 50)
    starter_menu = StarterMenu(screen,
                               [Button("Pokemon 1",(150,215),(300,300), text = "Pokemon 1", color = WHITE,font_color= BLACK), 
                                Button("Pokemon 2",(500,215),(300,300), text = "Pokemon 2",color = BLACK),
                                Button("Pokemon 3",(850,215),(300,300),text = "Pokemon 3",color = PURPLE)],
                                user,
                                fonts
                                )
    starter_menu.run()
if __name__ == "__main__":

    main()