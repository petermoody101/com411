from OOP.human import Human
from OOP.robot import Robot
#defining a class
class Planet:
  inhabitants = {
    "humans" : [],
    "robots" : []
  }
  #defining an instance
  def __init__(self, name = "Planet"):
    self.name = name
  #defining instance methods
  def add_human(self, human):
    Planet.inhabitants["humans"].append(human)
  
  def remove_human(self, human):
    Planet.inhabitants["humans"].remove(human)
  
  def add_robot(self, robot):
    Planet.inhabitants["robots"].append(robot)
  
  def remove_robot(self, robot):
    Planet.inhabitants["robots"].remove(robot)

  def __repr__(self):
    return(f"planet {self.name}, humans {Planet.inhabitants['humans']}, robots {Planet.inhabitants['robots']}")

  def __str__(self):
    return(f"The planet {self.name} contains the following humans {Planet.inhabitants['humans']} and the following robots {Planet.inhabitants['robots']}")
