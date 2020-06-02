'''
    Collider class file
    Pygame "engine"
    Designed to test different effects
'''
import pygame
from pygame.math import Vector2
from engine.behaviour import Behaviour

class BoxCollider(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "BoxCollider"
        self.is_trigger = False
        self.center = Vector2()
        self.offset = Vector2()
        self.extent = Vector2()
        self.box = pygame.Rect(0,0,0,0)
        self.is_debug = False
    def update(self):
        super().update()
        t = self.game_object.get_behaviour("Transform")
        self.center = Vector2(t.position)
        self.center.x += self.offset.x
        self.center.y += self.offset.y
        self.box.center = self.center
        self.box.width = int(self.extent.x)
        self.box.height = int(self.extent.y)
    def render(self):
        super().render()
        if self.is_debug:
            surf = pygame.display.get_surface()
            pygame.draw.rect(surf, (0, 255, 0), self.box, 2)
    #collider-specific methods
        #overlaps() is designed for AABB only
    def overlaps(self, other):
        if isinstance(other, BoxCollider):
            return self.box.colliderect(other.box)
    #WIP
    #prevent_overlap forces the current box away from the other
    def prevent_overlap(self, other):
        if (isintance(other, BoxCollider) and
            self.box.colliderect(other.box)):
            r = self.box.clip(other.box)
            t = self.game_object.get_behaviour("Transform")
