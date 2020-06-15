'''
    Shield Renderer Class
    pygame "engine"
    Designed to test different effects
'''
import pygame
from engine.behaviour import Behaviour

class ShieldRenderer(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "ShieldRenderer"
        self.colour = (0, 255, 255, 127)
        self.thickness = 4
        self.radius = 100
        self.shield_is_on = False
        self.display_shield = False
    def start(self):
        super().start()
    def update(self):
        super().update()
    def render(self):
        surf = pygame.display.get_surface()
        t = self.game_object.get_behaviour("Transform")
        center = (int(t.position.x), int(t.position.y))

        if self.shield_is_on:
            if self.display_shield:
                pygame.draw.circle(surf, self.colour, center,
                                   self.radius, self.thickness)
            self.display_shield = not self.display_shield
