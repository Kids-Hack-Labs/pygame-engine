'''
    ***Game class file***
    Pygame "engine"
    Designed to test different effects
'''
import sys, pygame

#Other imports go here
from test_screen import TestScreen

class Game:
    class __Game:
        current_screen = None #static variable
        
        def __init__(self, _width, _height, _title):
            pygame.init()

            self.window_size = _width, _height
            self.caption = _title
            
            pygame.display.set_mode(self.window_size)
            pygame.display.set_caption(self.caption)
            Game.__Game.current_screen = TestScreen()
            self.is_running = True

        def run(self):
            while self.is_running:
                #start is passed after the first time
                Game.__Game.current_screen.start()
                self.process_events()
                self.update()
                self.render()
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

        @staticmethod
        def set_screen(_screen):
            Game.__Game.current_screen = _screen
            #current_screen.start()

    instance = None #Game's point of access

    def __init__(self, _width, _height, _title):
        if not Game.instance:
            Game.instance = Game.__Game(_width,
                                        _height,
                                        _title)
        else:
            pass
            
    def __getattr__(self, name):
        return getattr(self.instance, name)
