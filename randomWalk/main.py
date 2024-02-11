import pygame
from walker import Walker
from screenWalker import ScreenWalker

pygame.init()

if __name__ == '__main__':
    screenConfig = (800, 600, 30)
    screen = ScreenWalker(screenConfig[0], screenConfig[1], screenConfig[2], 'A Traditional Random Walk')
    walker = Walker(screenConfig[2])

    while True:
        walker.step()

        screen.changePixelColor(walker.getX(), walker.getY())
        screen.draw()

        screen.event()
        pygame.time.Clock().tick(60)
