'''
    Intro Screen
    KHL Engine
    Designed to showcase different effects
'''
#Base imports
import pygame
from engine.screen import Screen
from engine.game_object import GameObject
from engine.text_renderer import TextRenderer
#Behaviour imports
from engine.box_collider import BoxCollider
from src.button_behaviour import ButtonBehaviour
from src.button_renderer import ButtonRenderer
#Convenience imports
from pygame.math import Vector2
from pygame import Color

class IntroScreen(Screen):
    def __init__(self):
        super().__init__()
        self.bg_colour = (127, 0, 255)
    def start(self):

        #Text GO
        text_go = GameObject()
        text_go.name = "Title"
        text_go.get_behaviour("Transform").position = Vector2(512, 250)
        text_go.add_behaviour(TextRenderer())
        text_go.get_behaviour("TextRenderer").text = "Random Game"
        text_go.get_behaviour("TextRenderer").set_size(63)
        self.add_game_object(text_go)
        #button GO

        button_go = GameObject()
        button_go.name = "StartButton"
        button_go.get_behaviour("Transform").position = Vector2(512, 475)
        button_go.add_behaviour(BoxCollider())
        button_go.add_behaviour(ButtonBehaviour())
        button_go.add_behaviour(ButtonRenderer())
        button_go.add_behaviour(TextRenderer())
        button_go.get_behaviour("TextRenderer").text = "START"
        button_go.get_behaviour("TextRenderer").set_size(50)
        self.add_game_object(button_go)
        super().start()
    def update(self):
        super().update()
    def render(self):
        screen = pygame.display.get_surface()
        if self.bg_colour != None:
            screen.fill(self.bg_colour)
        if self.image != None:
            screen.blit(self.image)
        #Remove later
        sq = screen.get_rect()
        w = int(sq.width)
        hw = int(sq.width/2)
        h = int(sq.height)
        hh = int(sq.height/2)
        pygame.draw.line(screen, (0, 0, 0), (hw, 0), (hw, h))
        pygame.draw.line(screen, (0, 0, 0), (0, hh), (w, hh))
        super().render()
