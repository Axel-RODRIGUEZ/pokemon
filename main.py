import json
import pygame
from os import path
from src.button import Button
from src.pokemon import Pokemon

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
    running = True

    while running:
        screen.fill((202,228,241))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        clock.tick(60)
        pygame.display.update()

    pygame.quit()
   

if __name__ == "__main__":

    main()