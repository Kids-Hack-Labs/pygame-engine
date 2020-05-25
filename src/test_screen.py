'''
    ***Test Screen class***
    Pygame "engine"
    Designed to test a couple effects
'''
import pygame
from engine.screen import Screen
from engine.game_object import GameObject
#Behaviour Imports
from src.rect_renderer import RectRenderer
from src.ship_renderer import ShipRenderer
from src.movement import Movement
from src.shield_renderer import ShieldRenderer
from src.ship_commands import ShipCommands

class TestScreen(Screen):
    def __init__(self):
        super().__init__()

    def start(self):
        self.image = pygame.image.load("assets/Images/Space.jpg")
        test_go = GameObject()
        test_go.name = "Ship"
        test_go.get_behaviour("Transform").position.x = 512
        test_go.get_behaviour("Transform").position.y = 388
        test_go.add_behaviour(ShipRenderer())
        test_go.add_behaviour(ShieldRenderer())
        test_go.add_behaviour(Movement())
        test_go.add_behaviour(ShipCommands())
        self.add_game_object(test_go)
        super().start()
        
    def update(self):
        super().update()
        
    def render(self):
        surf = pygame.display.get_surface()
        if self.bg_colour != None:
            surf.fill(self.bg_colour)
        if self.image != None:
            surf.blit(self.image, (0, 0))
        super().render()
        
    def add_game_object(self, game_object):
        super().add_game_object(game_object)
        
    def remove_game_object(self, game_object):
        super().remove_game_object(game_object)
