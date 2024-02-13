from random import randint
class RandomDistribution:
    def __init__(self, totalRandomCounts):
        self.__totalRandomCounts = totalRandomCounts
        self.__randomCounts = [0] * totalRandomCounts

    def randomCount(self):
        index = randint(0, self.__totalRandomCounts - 1)
        self.__randomCounts[index] += 1

        return self.__randomCounts
