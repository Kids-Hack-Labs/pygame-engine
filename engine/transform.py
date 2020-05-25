'''
    Transform class file
    Pygame "engine"
    Designed to test different effects
'''
import pygame
from pygame.math import Vector2
from engine.behaviour import Behaviour

class Transform(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "Transform"
        self.parent = None
        self.position = Vector2()
        self.rotation = 0
        self.scale = Vector2(1,1)
    def update(self):
        pass
    def render(self):
        pass

    #Transform specific functionality
    def translate(self, translation):
        if isinstance(translation, Vector2):
            self.position.x += translation.x
            self.position.y += translation.y
            return #safety measure
        if isinstance(translation, (list, tuple)):
            self.position.x += translation[0]
            self.position.y += translation[1]
            return #safety measure
    def rotate(self, _rotation):
        self.rotation += _rotation
