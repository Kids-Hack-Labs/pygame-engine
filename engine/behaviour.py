'''
    Behaviour Base Class file
    Pygame "engine"
    Designed to test different effects
'''

class Behaviour:
    def __init__(self):
        self.name = ""
        self.game_object = None
        self.is_active = True
    def update(self):
        pass
    def render(self):
        pass
