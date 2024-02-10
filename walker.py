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
        if self.__x < 0:
            self.__x = 0
        if self.__x > self.__pixel - 1:
            self.__x = self.__pixel - 1

        if self.__y < 0:
            self.__y = 0
        if self.__y > self.__pixel - 1:
            self.__y = self.__pixel - 1

        choice = randint(0, 3)
        if choice == 0:
            self.__x += 1
        elif choice == 1:
            self.__x -= 1
        elif choice == 2:
            self.__y += 1
        elif choice == 3:
            self.__y -= 1

        if self.__x < 0 or self.__x > (self.__pixel - 1) or self.__y < 0 or (self.__y > self.__pixel - 1):
            self.step()
