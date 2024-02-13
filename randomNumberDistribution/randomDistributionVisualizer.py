import pygame
from utils.object import Object
from randomDistribution import RandomDistribution

WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)


class RandomDistributionVisualizer(Object):
    def __init__(self, width, height, totalRandomCounts=20):
        super().__init__()
        self.__columnsHeight = height
        self.__columnsWidth = width / totalRandomCounts
        self.__randomDistribution = RandomDistribution(totalRandomCounts)

    def draw(self, pygameDisplay):
        randomCount = self.__randomDistribution.randomCount()

        for c in range(0, len(randomCount)):
            rect = pygame.Rect(c * self.__columnsWidth, self.__columnsHeight - randomCount[c],
                               self.__columnsWidth, self.__columnsHeight)
            pygame.draw.rect(pygameDisplay, BLACK, rect, 1)
