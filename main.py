import pygame
from constants import *


def main():
    pygame.init()
    screen()
    start_game()
    
    



def start_game():
    """This function will initialize the game"""
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} ")
    print(f"Screen height: {SCREEN_HEIGHT} ")
    window = True
    while window:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            keep_60_fps()



def screen():
    """Create a black screen"""
    black = (0, 0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(black)
    pygame.display.flip()


def keep_60_fps():
    """This function will make sure that the game maintains 60 fps"""
    time = pygame.time.Clock()
    dt = 0
    tick = time.tick(60)
    dt = tick / 1000



    

     













if __name__ == "__main__":
    main()