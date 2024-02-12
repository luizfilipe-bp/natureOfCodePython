import pygame
import sys
from utils.object import Object
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

        self.__screenObjects = [Object()]

    def __drawObjects(self):
        for screenObject in self.__screenObjects:
            screenObject.draw(self.pygameDisplay)

    def draw(self):
        self.pygameDisplay.fill(self.__backgroundColor)
        self.__drawObjects()
        pygame.display.flip()

    def getHeight(self):
        return self.__height

    def addScreenObject(self, screenObject):
        # TODO: substituir por tratamento de erro
        if isinstance(screenObject, Object):
            self.__screenObjects.append(screenObject)

    @staticmethod
    def event():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        self.draw()
        self.event()
        pygame.time.Clock().tick(60)
