import pygame
from constants import *
from player import *


def main():
        pygame.init()
        player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        start_game(player1)
        
    


def start_game(player):
    """This function will initialize the game"""
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} ")
    print(f"Screen height: {SCREEN_HEIGHT} ")
    black = (0, 0, 0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(black)
    player.draw(screen)
    pygame.display.flip()
    window = True
    while window:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            player.update()
            keep_60_fps()
        player.draw(screen)





def keep_60_fps():
    """This function will make sure that the game maintains 60 fps"""
    time = pygame.time.Clock()
    dt = 0
    tick = time.tick(60)
    dt = tick / 1000



    

     













if __name__ == "__main__":
    main()