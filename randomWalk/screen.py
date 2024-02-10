import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Screen:
    def __init__(self, width, height, pixel=100, name='Screen'):
        self.__width = width
        self.__height = height
        self.__pixel = pixel  # pixel quantity
        self.__name = name

        self.pygameDisplay = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption(self.__name)

        self.pixelWidth = width // self.__pixel
        self.pixelHeight = height // self.__pixel
        self.backgroundColor = WHITE
        self.matrix = [[self.backgroundColor] * self.__pixel for _ in range(self.__pixel)]

    def draw(self):
        for line in range(self.__pixel):
            for row in range(self.__pixel):
                pygame.draw.rect(self.pygameDisplay, self.matrix[line][row],
                                 (row * self.pixelWidth, line * self.pixelHeight, self.pixelWidth, self.pixelHeight))
        pygame.display.flip()
        self.pygameDisplay.fill(self.backgroundColor)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
        decrease = 51
        if actualColor[0] - decrease >= 0:
            self.matrix[x][y] = (actualColor[0] - decrease, actualColor[0] - decrease, actualColor[0] - decrease)

