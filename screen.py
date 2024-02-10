import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Screen:
    def __init__(self, width, height, pixel=100, name='Screen'):
        self.width = width
        self.height = height
        self.pixel = pixel  # pixel quantity
        self.name = name

        self.pygameDisplay = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)

        self.pixelWidth = width // self.pixel
        self.pixelHeight = height // self.pixel
        self.backgroundColor = WHITE
        self.matrix = [[self.backgroundColor] * self.pixel for _ in range(self.pixel)]

    def draw(self):
        for line in range(self.pixel):
            for row in range(self.pixel):
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
        print(f'{x}, {y}')
        if actualColor[0] - 15 >= 0:
            self.matrix[x][y] = (actualColor[0] - 15, actualColor[0] - 15, actualColor[0] - 15)
        print(actualColor)

