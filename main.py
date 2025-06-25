import pygame
from constants import *
black = (0, 0, 0)
window = True


def main():
    pygame.init()
    test_function()
    print(f"Screen width: {SCREEN_WIDTH} ")
    print(f"Screen height: {SCREEN_HEIGHT} ")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while window:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.fill(black)
            pygame.display.flip()





def test_function():
        print("Starting Asteroids!")
















if __name__ == "__main__":
    main()