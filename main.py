import pygame
from os import path
from src.MainMenu import MainMenu
from src.User import User
from src.Button import Button

def main():

    BASE_DIR = path.dirname(path.abspath(__file__))
    FONT_PATH = path.join(BASE_DIR, "assets", "fonts", "LiberationSans-Regular.ttf")
    UI_IMAGES_PATH = path.join(BASE_DIR, "assets", "images", "ui", "menu")

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Pokemon')
    
    screen = pygame.display.set_mode((1300, 731))
    clock = pygame.time.Clock()
    fonts = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50)

    user = User(is_new=False)
    menu = MainMenu(screen, 
                    [Button("battle", 
                            (500,450), 
                            text="Lancer une partie", 
                            bg_image=pygame.image.load(path.join(UI_IMAGES_PATH, "button.png")), 
                            hover_bg_image=pygame.image.load(path.join(UI_IMAGES_PATH, "hover_button.png"))),
                    Button("add_pokemon", (500,550), 
                           text="Ajouter un Pokémon", 
                           bg_image=pygame.image.load(path.join(UI_IMAGES_PATH, "button.png")), 
                           hover_bg_image=pygame.image.load(path.join(UI_IMAGES_PATH, "hover_button.png"))),
                    Button("pokedex", (500,650), 
                           text="Accéder au Pokédex", 
                           bg_image=pygame.image.load(path.join(UI_IMAGES_PATH, "button.png")), 
                           hover_bg_image=pygame.image.load(path.join(UI_IMAGES_PATH, "hover_button.png")))], 
                    user, 
                    fonts)
    menu.run()
   
if __name__ == "__main__":

    main()