from utils.object import Object
import pygame
from walker import Walker

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class WalkerMatrix(Object):
    def __init__(self, width, height, pixel=50):
        super().__init__()
        self.__pixel = pixel
        self.__matrixColor = WHITE
        self.__matrix = [[self.__matrixColor] * self.__pixel for _ in range(self.__pixel)]

        self.__pixelWidth = width // pixel
        self.__pixelHeight = height // pixel

        self.__walker = Walker(pixel)

    def draw(self, pygameDisplay):
        self.__walker.step()
        self.changePixelColor(self.__walker.getX(), self.__walker.getY())

        for line in range(self.__pixel):
            for row in range(self.__pixel):
                pygame.draw.rect(pygameDisplay, self.__matrix[line][row],
                                 (row * self.__pixelWidth, line * self.__pixelHeight,
                                  self.__pixelWidth, self.__pixelHeight))

    def mouseDetection(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                line = y // self.__pixelHeight
                row = x // self.__pixelWidth
                self.__matrix[line][row] = BLACK

    def changePixelColor(self, x, y):
        self.__whiteToBlack(x, y)

    def __whiteToBlack(self, x, y):
        actualColor = self.__matrix[x][y]
        newColor = actualColor[0] - 51
        if newColor >= 0:
            self.__matrix[x][y] = (newColor, newColor, newColor)
