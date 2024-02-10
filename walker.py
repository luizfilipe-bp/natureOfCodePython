from random import randint


class Walker:
    def __init__(self, width, height, pixel=100):
        self.x = pixel // 2
        self.y = pixel // 2
        self.pixel = pixel
        print(f'x: {self.x}, y: {self.y}')

    def step(self):
        if self.x < 0:
            self.x = 0
        if self.x > self.pixel - 1:
            self.x = self.pixel - 1

        if self.y < 0:
            self.y = 0
        if self.y > self.pixel - 1:
            self.y = self.pixel - 1

        choice = randint(0, 3)
        if choice == 0:
            self.x += 1
        elif choice == 1:
            self.x -= 1
        elif choice == 2:
            self.y += 1
        elif choice == 3:
            self.y -= 1

        if self.x < 0 or self.x > (self.pixel - 1) or self.y < 0 or (self.y > self.pixel - 1):
            self.step()
