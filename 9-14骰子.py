# -*- coding: UTF-8 -*-
from random import randint


class Die():
    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print(str(x))

die1 = Die(20)
die1.roll_die()