'''
    Game Class
    Responsible for managing windows and responding to
    OS events.
    Initializes game and cleans it up
'''
import sys, pygame

class Game:
    def __init__(self, size, title):
        self.window_size = size
        self.game_title = title

        pygame.init()
    
        pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.game_title)

        self.screens = []

        self.is_running = True
    
    def run(self):
        while self.is_running:
            for evt in pygame.event.get():
                if evt == pygame.QUIT:
                    self.is_running = False
                    self.cleanup()
                    pygame.quit()
                    sys.exit()
    def cleanup(self):
        pass
