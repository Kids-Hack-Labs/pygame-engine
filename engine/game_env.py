'''
    ***Game class file***
    KHL Engine
    Created       May 03, 2020
    Last Modified Jun 04, 2020

    Remarks:
    -> Implemented as a singleton
    -> Manages Window instantiation, the Game Loop
       (event processing, update, render),
       and performs cleanup functions on exit
'''
#basic imports
import sys, pygame
#Frame rate spec
_FPS = 30

#Other imports go here
from src.test_screen import TestScreen

class Game:
    #The "real" Game class is wrapped in a singleton
    #manager who controls access to it. Since it begins
    #with a double underscore, it is treated as
    #a class-private class, which encapsulates its
    #data and functionality
    class __Game:
        current_screen = None #static variable
        
        def __init__(self, _size, _title):
            #Game time management variables
            self.is_started = False
            self.is_running = False
            self.time_since_started = 0
            self.delta_time = 0

            #pygame and game clock initialization
            pygame.init()
            self.game_clock = pygame.time.Clock()

            #Window specs
            self.window_size = _size
            self.caption = _title
            
            pygame.display.set_mode(self.window_size)
            pygame.display.set_caption(self.caption)

            #A single screen can be loaded at a time
            #as a static variable.
            Game.__Game.current_screen = TestScreen()

            self.time_since_started = pygame.time.get_ticks()

            #assuming everything is okay
            self.is_running = True

        def run(self):
            #This initial check is aimed at preventing
            #multiple runs of the same game.
            if self.is_started:
                return
            self.is_started = True

            #Here is where the game loop "proper" begins
            while self.is_running:
                #start is passed after the first time
                if not Game.__Game.current_screen.started:
                    Game.__Game.current_screen.start()
                self.process_events()
                self.update()
                self.render()
                #simplified timer/framerate implementation
                self.delta_time = self.game_clock.tick(_FPS)
                self.time_since_started = pygame.time.get_ticks()
            self.cleanup()

        # called when the game recieves a mouse click
        def handle_mouse(self):
            self.current_screen.on_mouse_click(pygame.mouse.get_pos())

        def process_events(self):
            #Other event processing may go here, if needed
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    self.is_running = False
                if evt.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse()

        def update(self):
            Game.__Game.current_screen.update()

        def render(self):
            Game.__Game.current_screen.render()
            pygame.display.flip()

        def cleanup(self):
            pygame.quit()
            sys.exit()

        def get_delta_time(self):
            return self.delta_time

        #This allows for screen change
        @staticmethod
        def set_screen(_screen):
            Game.__Game.current_screen = _screen

    #Game's point of access
    instance = None 

    #outer Game class methods:
    def __init__(self, _size, _title):
        if not Game.instance:
            Game.instance = Game.__Game(_size,
                                        _title)
        else:
            pass

    #part of the singleton code
    def __getattr__(self, name):
        return getattr(self.instance, name)
