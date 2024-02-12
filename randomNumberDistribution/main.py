import pygame
from screenRandomDistribution import ScreenRandomDistribution

if __name__ == '__main__':
    screen = ScreenRandomDistribution(1200, 600, 'A Random-Number Distribution', 25)
    while True:
        screen.draw()

        screen.event()

        pygame.time.Clock().tick(60)
