from random import randint


class Walker:
    def __init__(self, pixel=100):
        self.__x = pixel // 2
        self.__y = pixel // 2
        self.__pixel = pixel

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def step(self):
        stepX = randint(-1, 1)
        if 0 <= self.__x + stepX < self.__pixel:
            self.__x += stepX

        stepY = randint(-1, 1)
        if 0 <= self.__y + stepY < self.__pixel:
            self.__y += stepY
