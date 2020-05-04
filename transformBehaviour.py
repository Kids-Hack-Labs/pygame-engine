import pygame, sys

class Transform:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, target):
        self.x += target[0]
        self.y -= target[1]


class Character:
    def __init__(self, x, y):
        self.fly = False
        self.die = False
        self.up = False
        self.down = False


    def dead(self):
        self.die = True



            
        
