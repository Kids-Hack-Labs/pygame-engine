'''
    Ship Commands class
    pygame "engine"
    Designed to test different effects
'''
import pygame
from engine.behaviour import Behaviour

class ShipCommands(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "ShipCommands"
        #self.cooldown = 
    def update(self):
        key_list = pygame.key.get_pressed()

        space = key_list[pygame.K_SPACE]

        #simplified
        self.deploy_shield(space)

    def render(self):
        super().render()

    def deploy_shield(self, activate):
        renderer = self.game_object.get_behaviour("ShieldRenderer")

        if renderer != None:
            renderer.shield_is_on = activate
            
