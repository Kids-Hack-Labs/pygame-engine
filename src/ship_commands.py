'''
    Ship Commands class
    pygame "engine"
    Designed to test different effects
'''
import pygame
from engine.behaviour import Behaviour
from src.bullet_movement import BulletMovement
from src.bullet_renderer import BulletRenderer

class ShipCommands(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "ShipCommands"
        self.cooldown = 250 #milliseconds
        self.has_shot = False
        self.last_shot = 0
        self.bullet_counter = 0
    def start(self):
        super().start()
    def update(self):
        super().update()
        key_list = pygame.key.get_pressed()

        shield_key = key_list[pygame.K_j]
        shoot_key = key_list[pygame.K_SPACE]

        self.deploy_shield(shield_key)

        #simplified, but necessary for clock
        from engine.game_env import Game

        if self.has_shot:
            self.last_shot += Game.instance.get_delta_time()
        if self.last_shot > self.cooldown:
            self.last_shot = 0
            self.has_shot = False
        if shoot_key and not self.has_shot:
            self.shoot()

    def render(self):
        super().render()

    def deploy_shield(self, activate):
        renderer = self.game_object.get_behaviour("ShieldRenderer")

        if renderer != None:
            renderer.shield_is_on = activate

    def shoot(self):
        self.has_shot = True

        from engine.game_object import GameObject
        
        bullet = GameObject()
        bullet.name = "Bullet"+str(self.bullet_counter)
        bullet.get_behaviour("Transform").position.x = self.game_object.get_behaviour("Transform").position.x
        bullet.get_behaviour("Transform").position.y = self.game_object.get_behaviour("Transform").position.y
        bullet.get_behaviour("Transform").rotation = self.game_object.get_behaviour("Transform").rotation
        bullet.add_behaviour(BulletMovement())
        bullet.add_behaviour(BulletRenderer())
        
        GameObject.add_to_screen(bullet)
        self.bullet_counter += 1
