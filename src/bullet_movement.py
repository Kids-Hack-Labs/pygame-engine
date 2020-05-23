'''
    Bullet Movement class
    pygame "engine"
'''
import math
from engine.behaviour import Behaviour

class BulletMovement(Behaviour):
    def __init__(self):
        super().__init__()
        self.speed = 15

    def update(self):
        super().update()
        t = self.game_object.get_behaviour("Transform")
        rot = math.radians(t.rotation)
        target = [0,0]
        target[0] = -1*self.speed*math.sin(rot)
        target[1] = -1*self.speed*math.cos(rot)
        t.translate(target)

    def render(self):
        super().render()
