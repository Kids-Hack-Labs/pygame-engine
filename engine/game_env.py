'''
    ***Game class file***
    Pygame "engine"
    Designed to test different effects
'''
import sys, pygame
#Frame rate spec
_FPS = 30

#Other imports go here
from src.test_screen import TestScreen



class Game:
    class __Game:
        current_screen = None #static variable
        
        def __init__(self, _size, _title):
            self.is_started = False
            self.is_running = False
            self.time_since_started = 0
            self.delta_time = 0
            pygame.init()

            self.game_clock = pygame.time.Clock()

            self.window_size = _size
            self.caption = _title
            
            pygame.display.set_mode(self.window_size)
            pygame.display.set_caption(self.caption)
            Game.__Game.current_screen = TestScreen()

            self.time_since_started = pygame.time.get_ticks()
            #assuming everything is okay
            self.is_running = True

        def run(self):
            if self.is_started:
                return #this prevents multiple runs
            self.is_started = True
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

        def process_events(self):
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    self.is_running = False

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

        @staticmethod
        def set_screen(_screen):
            Game.__Game.current_screen = _screen
            #current_screen.start()

    instance = None #Game's point of access

    def __init__(self, _size, _title):
        if not Game.instance:
            Game.instance = Game.__Game(_size,
                                        _title)
        else:
            pass
            
    def __getattr__(self, name):
        return getattr(self.instance, name)
