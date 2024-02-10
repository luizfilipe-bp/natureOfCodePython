import pygame
from walker import Walker
from screen import Screen
from time import sleep

# Inicialização do Pygame
pygame.init()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    screenConfig = (800, 600, 5)
    screen = Screen(screenConfig[0], screenConfig[1], screenConfig[2], 'A Traditional Random Walk')
    walker = Walker(screenConfig[0], screenConfig[1], screenConfig[2])

    while True:
        walker.step()
        screen.changePixelColor(walker.x, walker.y)
        screen.draw()

        screen.event()

