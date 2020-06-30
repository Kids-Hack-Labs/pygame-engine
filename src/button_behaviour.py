'''
    Custom Button Behaviour Class
    KHL Engine
    Designed to render a different kind of button
'''
import pygame
from engine.behaviour import Behaviour

class ButtonBehaviour(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "ButtonBehaviour"
        self.is_hover = False
        self.is_released = False
        self.is_pressed = False

        self.box_collider = None
    def start(self):
        self.box_collider = self.game_object.get_behaviour("BoxCollider").box
        super().start()
    def update(self):
        super().update()
        self.is_hover = self.box_collider.collidepoint(pygame.mouse.get_pos())
    def render(self):
        super().render()
        if self.is_hover:
            print("There's a mouse here...")
