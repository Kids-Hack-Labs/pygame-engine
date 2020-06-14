import pygame
from engine.behaviour import Behaviour

class TextRenderer(Behaviour):
    def __init__(self):
        super().__init__()
        self.name = "TextRenderer"

        self.text = "Hello, World!"
        self.size = 12
        self.colour = (255, 255, 255)
        self.font_path = "engine/engine_assets/Roboto-Medium.ttf"

        self.do_antialias = True

        self.generate_font()
        self.display = pygame.display.get_surface()

        self.transform = None

    def start(self):
        self.transform = self.game_object.get_behaviour("Transform")

    def generate_font(self):
        self.font = pygame.font.Font(self.font_path, self.size)

    # need to update the font through this method since we don't want
    # to create a new font object every frame
    def set_size(self, size):
        self.size = size

        self.generate_font()

    def set_font(self, sfont_path):
        pass
        
    def update(self):
        pass
        
    def render(self):
        text_surface = self.font.render(self.text, self.do_antialias, self.colour)
        self.display.blit(text_surface, self.transform.position)
        
