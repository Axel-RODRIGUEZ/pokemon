import pygame
from os import path,pardir

BASE_DIR = path.dirname(path.abspath(__file__))
FONT_PATH = path.join(BASE_DIR, pardir, "assets", "fonts", "LiberationSans-Regular.ttf")

def main():

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Pokemon')
    window = pygame.display.set_mode((1300, 731))
    clock = pygame.time.Clock()
    fonts = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50)

    

if __name__ == "__main__":

    main()