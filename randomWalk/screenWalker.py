import pygame
from utils.screen import Screen

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class ScreenWalker(Screen):
    def __init__(self, width, height, name='A Traditional Random Walk', pixel=100):
        super().__init__(width, height, name)
        self.__pixel = pixel  # pixel * pixel matrix

        self.pixelWidth = width // self.__pixel
        self.pixelHeight = height // self.__pixel
        self.matrixColor = WHITE
        self.matrix = [[self.matrixColor] * self.__pixel for _ in range(self.__pixel)]

    def draw(self):
        for line in range(self.__pixel):
            for row in range(self.__pixel):
                pygame.draw.rect(self.pygameDisplay, self.matrix[line][row],
                                 (row * self.pixelWidth, line * self.pixelHeight, self.pixelWidth, self.pixelHeight))
        pygame.display.flip()

    def mouseDetection(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                line = y // self.pixelHeight
                row = x // self.pixelWidth
                self.matrix[line][row] = BLACK

    def changePixelColor(self, x, y):
        self.whiteToBlack(x, y)

    def whiteToBlack(self, x, y):
        actualColor = self.matrix[x][y]
        newColor = actualColor[0] - 51
        if newColor >= 0:
            self.matrix[x][y] = (newColor, newColor, newColor)
