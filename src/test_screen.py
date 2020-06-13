'''
    ***Test Screen class***
    Pygame "engine"
    Designed to test a couple effects
'''
import pygame
from engine.screen import Screen
from engine.game_object import GameObject
from engine.box_collider import BoxCollider
#Behaviour Imports
from src.rect_renderer import RectRenderer
from src.ship_renderer import ShipRenderer
from src.movement import Movement
from src.shield_renderer import ShieldRenderer
from src.ship_commands import ShipCommands
#Convenience imports
from pygame.math import Vector2
from pygame import Rect

class TestScreen(Screen):
    def __init__(self):
        super().__init__()

    def start(self):
        self.image = pygame.image.load("assets/images/space.jpg")
        test_go = GameObject()
        test_go.name = "Ship"
        test_go.get_behaviour("Transform").position.x = 512
        test_go.get_behaviour("Transform").position.y = 388
        test_go.add_behaviour(BoxCollider())
        test_go.get_behaviour("BoxCollider").is_debug = False
        test_go.get_behaviour("BoxCollider").extent = pygame.math.Vector2(150)
        test_go.add_behaviour(ShipRenderer())
        test_go.add_behaviour(ShieldRenderer())
        test_go.add_behaviour(Movement())
        test_go.add_behaviour(ShipCommands())
        self.add_game_object(test_go)

        another_go = GameObject()
        another_go.name = "Obstacle"
        another_go.get_behaviour("Transform").position.x = 200
        another_go.get_behaviour("Transform").position.y = 200
        another_go.add_behaviour(BoxCollider())
        another_go.get_behaviour("BoxCollider").is_debug = True
        another_go.get_behaviour("BoxCollider").extent = Vector2(350)
        self.add_game_object(another_go)

        overlap_go = GameObject()
        overlap_go.name = "Overlap"
        overlap_go.add_behaviour(RectRenderer())
        overlap_go.get_behaviour("RectRenderer").colour = (255, 0, 0)
        overlap_go.get_behaviour("RectRenderer").rect = Rect(0, 0, 0, 0)
        self.add_game_object(overlap_go)
        super().start()
        
    def update(self):
        super().update()
        ship_col = self.game_objects["Ship"].get_behaviour("BoxCollider")
        obstacle_col = self.game_objects["Obstacle"].get_behaviour("BoxCollider")
        ship_col.prevent_overlap(obstacle_col)
        result = ship_col.box.clip(obstacle_col.box)
        overlap = self.game_objects["Overlap"]
        overlap.get_behaviour("Transform").position = result.center
        overlap.get_behaviour("RectRenderer").rect = result
        
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
