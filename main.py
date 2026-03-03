import pygame
from os import path
from src.UserMenu import UserMenu
from src.Button import Button


def main():

       BASE_DIR = path.dirname(path.abspath(__file__))
       FONT_PATH = path.join(BASE_DIR, "assets", "fonts", "LiberationSans-Regular.ttf")
       UI_IMAGES_PATH = path.join(BASE_DIR, "assets", "images", "ui", "menu")
       POKEDEXS_PATH = path.join(BASE_DIR, "data", "pokedexs.json")
       SOUNDS_PATH = path.join(BASE_DIR, "assets", "sounds")
       MENU_MUSIC_PATH = path.join(SOUNDS_PATH, "ui", "crosscode-autumns-fall.mp3")

       if not path.exists(POKEDEXS_PATH):
              with open(POKEDEXS_PATH, "w") as file:
                     file.write("{}")
              print("New Pokedexs.json created.")
       else:
              print("Pokedexs.json data found.")

       pygame.init()
       pygame.mixer.init()
       pygame.mixer.music.load(MENU_MUSIC_PATH)
       pygame.display.set_caption('Pokemon')

       screen = pygame.display.set_mode((1300, 731))
       clock = pygame.time.Clock()
       fonts = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50), pygame.font.Font(FONT_PATH, 20)

       user_menu = UserMenu(screen,
                                   [Button("New Player",
                                          (500,444),
                                          (300,60), 
                                          text = "Nouvel Utilisateur",
                                          bg_image=pygame.image.load(path.join(UI_IMAGES_PATH, "button.png")), 
                                          hover_bg_image=pygame.image.load(path.join(UI_IMAGES_PATH, "hover_button.png"))), #décalage  20 pixels
                                   Button("Load save",
                                          (500,524),
                                          (300,60), 
                                          text = "Charger Partie",
                                          bg_image=pygame.image.load(path.join(UI_IMAGES_PATH, "button.png")), 
                                          hover_bg_image=pygame.image.load(path.join(UI_IMAGES_PATH, "hover_button.png"))),
                                   Button("Quit",
                                          (500,604),
                                          (300,60),
                                          text = "Quitter",
                                          bg_image=pygame.image.load(path.join(UI_IMAGES_PATH, "button.png")), 
                                          hover_bg_image=pygame.image.load(path.join(UI_IMAGES_PATH, "hover_button.png")))], #décalage 30 pixels
                                   fonts,
                                   clock
                                   )
       user_menu.run()

if __name__ == "__main__":

       main()