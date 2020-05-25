'''
    Ship Renderer class
    pygame "engine"
    Designed to test different effects
    THIS CODE REQUIRES HEAVY CLEANUP
'''
import pygame
from engine.behaviour import Behaviour

class ShipRenderer(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "ShipRenderer"
        #base image
        self.base_img = pygame.image.load("assets/Images/ships.bmp")
        #clipping rectangles for ship and fire
        self.ship_rect = pygame.Rect(0, 0, 256, 256)
        self.fire_rect = pygame.Rect(256, 0, 256, 256)
        #subsurfaces for ship and fire (clipping areas must be passed)
        self.ship_img = self.base_img.subsurface(self.ship_rect)
        self.fire_img = self.base_img.subsurface(self.fire_rect)
        
        self.display_fire = True

    def update(self):
        pass
    def render(self):
        #gets game surface and object's transform
        surf = pygame.display.get_surface()
        transf = self.game_object.get_behaviour("Transform")
        #creates rotated surfaces based on transform
        rotated_ship = pygame.transform.rotate(self.ship_img,
                                               transf.rotation).convert_alpha()
        rotated_fire = pygame.transform.rotate(self.fire_img,
                                               transf.rotation).convert_alpha()

        #Corrected rotation
        center_x = int(transf.position.x -
                       rotated_ship.get_rect().width/2)
        center_y = int(transf.position.y -
                       rotated_ship.get_rect().height/2)
        #actual draw to the screen, using properly rotated surfaces
        surf.blit(rotated_ship, (center_x, center_y),
                  rotated_ship.get_rect())
        #fire draw
        if self.display_fire:
            surf.blit(rotated_fire, (center_x, center_y),
                      rotated_fire.get_rect())
        self.display_fire = not self.display_fire
