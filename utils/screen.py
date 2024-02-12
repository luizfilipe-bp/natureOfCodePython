import pygame
import sys
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Screen:
    def __init__(self, width, height, name='Blank Screen'):
        self.__width = width
        self.__height = height
        self.__name = name
        self.__backgroundColor = WHITE

        self.pygameDisplay = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption(self.__name)

    def draw(self):
        self.pygameDisplay.fill(self.__backgroundColor)
        pygame.display.flip()

    def getHeight(self):
        return self.__height

    @staticmethod
    def event():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()