import pygame
from utils.screen import Screen
from randomDistributionVisualizer import RandomDistributionVisualizer

pygame.init()

if __name__ == '__main__':
    screenConfig = (1200, 600)
    screen = Screen(screenConfig[0], screenConfig[1], 'A Random-Number Distribution')

    randomDistribution = RandomDistributionVisualizer(screenConfig[0], screenConfig[1], 20)
    screen.addScreenObject(randomDistribution)

    while True:
        screen.run()
