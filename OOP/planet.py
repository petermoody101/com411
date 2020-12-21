from OOP.human import human
from OOP.robot import robot
#defining a class
class planet:
  inhabitants = {
    "humans" : [],
    "robots" : []
  }
  #defining an instance
  def __init__(self, name = "Planet"):
    self.name = name
  #defining instance methods
  def add_human(self, human):
    self.inhabitants["humans"].append(human)
  
  def remove_human(self, human):
    self.inhabitants["humans"].remove(human)
  
  def add_robot(self, robot):
    self.inhabitants["robots"].append(robot)
  
  def remove_robot(self, robot):
    self.inhabitants["robots"].remove(robot)

  def __repr__(self):
    return(f"planet {self.name}, humans {planet.inhabitants['humans']}, robots {planet.inhabitants['robots']}")

  def __str__(self):
    return(f"The planet {self.name} contains the following humans {planet.inhabitants['humans']} and the following robots {planet.inhabitants['robots']}")


planet = planet()
print(repr(planet))
peter = human("Peter")
ellie = human("Ellie")
planet.add_human(peter)
planet.add_human(ellie)
print(str(planet))
print(planet)