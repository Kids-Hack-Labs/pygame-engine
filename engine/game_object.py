'''
    ***Game class file***
    Authored by HErC
    Pygame "engine"
    Designed to test different effects
    The class follows a "behaviour-then-children"
    architecture. The reason is pretty much
    straightforward: any behaviour that alters
    the parent should be reflected in the children
'''
from engine.transform import Transform
class GameObject:
    def __init__(self):
        self.name = ""
        self.is_active = True
        self.children = {}
        self.behaviours = {}

        #all game objects should have a transform
        #used the GameObject's own add_behaviour
        #functionality, to ensure consistency
        self.add_behaviour(Transform())
        
    def update(self):
        #Opted for a behaviour-then-child architecture
        for behaviour_name in list(self.behaviours.keys()):
            if self.behaviours[behaviour_name].is_active:
                self.behaviours[behaviour_name].update()
        for child_name in self.children.keys():
            if self.children[child_name].is_active:
                self.children[child_name].update()

    def render(self):
        for behaviour_name in list(self.behaviours.keys()):
            if self.behaviours[behaviour_name].is_active:
                self.behaviours[behaviour_name].render()
        for child_name in self.children.keys():
            if self.children[child_name].is_active:
                self.children[child_name].render()

    #Behaviour management functionality
    def add_behaviour(self, behaviour):
        if (behaviour.name not in list(self.behaviours.keys())
            and behaviour.game_object == None):
            behaviour.game_object = self
            self.behaviours[behaviour.name] = behaviour

    def remove_behaviour(self, behaviour):
        if behaviour.name in list(self.behaviours.keys()):
            self.behaviours[behaviour.name].game_object = None
            self.behaviours.pop(behaviour.name)

    def get_behaviour(self, behaviour_name):
        if behaviour_name in self.behaviours.keys():
            return self.behaviours[behaviour_name]
        return None

    #Child management functionality
    def add_child(self, child):
        if (child.name not in self.children.keys()
             and child.parent != null):
            child.parent = self
            self.children[child.name] = child
