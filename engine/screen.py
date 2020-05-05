'''

    Screen class stores data about gameobjects on that screen.
    It worries about updating and rendering those objects.

    A "Game" instance typically includes more than one screen object.

    OBS: is_active should not be public... python :/

'''

import pygame

from game_object import GameObject

class Screen:

    def __init__(_game_objects = []):
        
        self.is_active = False
        self.game_objects = game_objects
    
    '''

    def get_active():
        return self.is_active

    def set_active(status):
        self.is_active = status

    '''

    # i suggest that we call this function if the game object has a render behaviour

    # if expects a render behaviour
    def render(self, render_behaviour = None):
        if not render_behaviour:
            print('No renderer on this GameObject!')
            return

        # call something like this
        # pygame.draw_sprite(render_behaviour.sprite)

    def update(self):

        # assuming here that the screen.update will only be called if
        # it is the currently active scene
        
        for game_object in self.game_objects:
            # could be changed to get_active()
            if game_object.is_active:
                game_object.update()

                # self.render(game_object.renderer())

        # currently the gameobject render function is an update duplicate!
                
