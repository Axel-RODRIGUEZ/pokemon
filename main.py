import pygame
from os import path
from src.button import Button

BASE_DIR = path.dirname(path.abspath(__file__))
FONT_PATH = path.join(BASE_DIR, "assets", "fonts", "LiberationSans-Regular.ttf")

def main():

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Pokemon')
    screen = pygame.display.set_mode((1300, 731))
    clock = pygame.time.Clock()
    fonts = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50)

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