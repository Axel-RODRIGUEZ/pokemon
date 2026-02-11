import json
import pygame
from os import path
from src.pokemon import Pokemon
from src.menu import Menu
from src.user import User
from src.button import Button

BASE_DIR = path.dirname(path.abspath(__file__))
FONT_PATH = path.join(BASE_DIR, "assets", "fonts", "LiberationSans-Regular.ttf")


with open ('data/pokemon.json','r', encoding="utf-8") as f:
    data_file = json.load(f)
def main():

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Pokemon')
    screen = pygame.display.set_mode((1300, 731))
    clock = pygame.time.Clock()
    fonts = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50)
    data = data_file[0]
    stats = data['stats']
    xp = 3000
    pokemon1= Pokemon(data['name']['fr'], stats['hp'], stats['atk'], stats['def'], stats['vit'], data["types"], xp)
    Pokemon.check_xp(pokemon1)
    print(pokemon1.level)

    user = User("Arthur")
    menu = Menu({"battle_mode": Button("battle", (200,200), text="Lancer une partie")}, user)
    menu.run()
   
if __name__ == "__main__":

    main()