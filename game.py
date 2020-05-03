import sys, pygame

class Game:
  def __init__(self, size, title):
    self.windowSize = size
    self.gameTitle = title

    pygame.init()
    
    pygame.display.set_mode(self.windowSize)
    pygame.display.set_caption(self.gameTitle)

    self.screens = []

    self.isRunning = True
    
  def run(self):
    while self.isRunning:
      for evt in pygame.event.get():
        if evt == pygame.QUIT:
          self.isRunning = False
          self.cleanup()
          pygame.quit()
          sys.exit()
  def cleanup(self):
    pass
