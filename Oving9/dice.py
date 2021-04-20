import random


class Dice:
    def __init__(self, sides_amount=6):
        self.__value = 1
        self.__sides = sides_amount

    @property
    def get_value(self):
        return self.__value

    @property
    def get_side_amount(self):
        return self.__sides

    def throw(self):
        self.__value = random.randint(1, self.__sides)
        return self.get_value

