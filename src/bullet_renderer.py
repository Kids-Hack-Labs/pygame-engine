'''
    Bullet renderer class
    pygame "engine" example
    Designed to test different functionality
'''
import pygame
from engine.behaviour import Behaviour

class BulletRenderer(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "BulletRenderer"
        self.colour = (255, 255, 0)
        self.radius = 5
    def update(self):
        super().update()
    def render(self):
        super().render()
        surf = pygame.display.get_surface()
        t = self.game_object.get_behaviour("Transform")
        center = (int(t.position.x), int(t.position.y))

        #render proper:
        pygame.draw.circle(surf, self.colour, center, self.radius)
