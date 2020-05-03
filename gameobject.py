'''
  Game Object base class
  Defines a basic Game Object structure for adding behaviours
  Because of its architecture, it assumes its first behaviour
  is a Transform.
  It expects behaviours to contain a flag to determine whether
  they are active or not.
  Overall, the code is designed to be behaviour-agnostic, but
  expects behaviours to have certain attributes, namely:
  is_active, game_object, (might include others in the future)

  OBS: because this is Python, name and is_active are public
'''
import pygame
#import behaviour
#from transformBehaviour import Transform

class GameObject:
  def __init__(self, _x = 0, _y = 0, _name = "",active = True):
    self.is_active = active
    self.name = _name
    self.behaviours = []
    #self.add_behaviour(Transform(_x, _y))

    #other initialization code goes here

  #Common functionality
  def update(self):
    for behaviour in self.behaviours:
      if behaviour.is_active:
        behaviour.update()

  def render(self):
    for behaviour in self.behaviours:
      if behaviour.is_active:
        behaviour.update()

  #Specific functionality
  def add_behaviour(self, behaviour):
    if behaviour not in self.behaviours:
      behaviour.game_object = self
      self.behaviours.append(behaviour)

  def remove_behaviour(self, behaviour):
    if behaviour in self.behaviours:
      self.behaviours.remove(behaviour)
      
  def get_transform(self):
    #OBS: expects Transform to be the first behaviour always
    return self.behaviours[0]

  #expects an empty object of target type for checking
  def get_behaviour(self, target_behaviour):
    for behaviour in self.behaviours:
      if type(behaviour) == type(target_behaviour):
        return behaviour
    return None #will require checks in other scripts
