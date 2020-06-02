'''
    Temporary Renderer Class file
    pygame "engine"
    Designed to test different effects   
'''
import pygame
from engine.behaviour import Behaviour

class RectRenderer(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "RectRenderer"
        self.colour = (255, 0, 0)
        self.rect = pygame.Rect(0, 0, 100, 100)
    def update(self):
        pass
    def render(self):
        surf = pygame.display.get_surface()
        t = self.game_object.get_behaviour("Transform")
        self.rect.center = (t.position[0], t.position[1])

        if (self.rect.width > 0 < self.rect.height):
            pygame.draw.rect(surf, self.colour, self.rect, 5)
