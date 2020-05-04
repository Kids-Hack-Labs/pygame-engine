'''


    OBS: is_active should not be public... python :/

'''

import pygame

class Screen:

    def __init__(game_objects):
        
        self.is_active = False
        self.game_objects = game_objects

    def set_active(status):
        self.is_active = status
