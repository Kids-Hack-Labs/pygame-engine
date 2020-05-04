class Behaviour:
    def __init__(self):
        self.game_object = None
        self.is_active = None

    def start(self):
        pass

    def update(self):
        pass


class Collision(Behaviour):
    def __init__(self, width, height):
        
        self.width == width
        self.height == height

class Active():
    def __init__(self, dimensions, sprite):
        self.sprite = sprite
        self.width = dimensions[0]
        self.height = dimensions[1]


class ActiveRender(Behaviour):
    def __init__(self, active):
        self.active = active

    def render(self):
        pass

    def update(self):
        pass
