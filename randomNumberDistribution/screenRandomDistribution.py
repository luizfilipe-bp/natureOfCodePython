import pygame
from utils.screen import Screen
from random import randint

WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)


class ScreenRandomDistribution(Screen):
    def __init__(self, width, height, name='A Random-Number Distribution', totalRandomCounts=20):
        super().__init__(width, height, name)

        self.totalRandomCounts = totalRandomCounts
        self.randomCounts = [0] * totalRandomCounts

        self.columnsWidth = self.__setColumnsWidth(width)

    def __setColumnsWidth(self, width):
        return width / self.totalRandomCounts

    def draw(self):
        screenHeight = self.getHeight()
        self.pygameDisplay.fill(WHITE)

        index = randint(0, self.totalRandomCounts - 1)
        self.randomCounts[index] += 1

        for c in range(0, self.totalRandomCounts):
            rect = pygame.Rect(c * self.columnsWidth, screenHeight - self.randomCounts[c],
                               self.columnsWidth, screenHeight)
            pygame.draw.rect(self.pygameDisplay, BLACK, rect, 1)

        pygame.display.flip()
