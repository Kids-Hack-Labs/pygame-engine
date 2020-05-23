'''
    ***Base Screen class file***
    Pygame "engine"
    Designed to test different effects
'''
import pygame
#other imports go here

class Screen:
    def __init__(self):
        self.bg_colour = None
        self.image = None
        self.game_objects = {}
        self.started = False
        
    def start(self):
        if not self.started:
            self.started = True
            return

    def update(self):
        #may have custom functionality in children
        for key in list(self.game_objects.keys()):
            if self.game_objects[key].is_active:
                self.game_objects[key].update()

    def render(self):
        #may have custom functionality in children
        #surf = pygame.display.get_surface()
        for key in list(self.game_objects.keys()):
            if self.game_objects[key].is_active:
                self.game_objects[key].render()

    def add_game_object(self, game_object):
        if game_object.name not in list(self.game_objects.keys()):
            self.game_objects[game_object.name] = game_object

    def remove_game_object(self, game_object):
        if game_object.name in list(self.game_objects.keys()):
            self.game_objects.pop(game_object.name)
