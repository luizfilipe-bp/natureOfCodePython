import pygame
from walkerMatrix import WalkerMatrix
from utils.screen import Screen

pygame.init()

if __name__ == '__main__':
    screenConfig = (800, 600, 150)
    screen = Screen(screenConfig[0], screenConfig[1], 'A Traditional Random Walk')

    walkerMatrix = WalkerMatrix(screenConfig[0], screenConfig[1], screenConfig[2])
    screen.addScreenObject(walkerMatrix)

    while True:
        screen.run()
