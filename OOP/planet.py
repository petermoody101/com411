<<<<<<< HEAD
from OOP.human import Human
from OOP.robot import Robot
#defining a class
class Planet:
=======
from OOP.human import human
from OOP.robot import robot
#defining a class
class planet:
>>>>>>> 725d7701e905c04d9678c9591772f140a373f274
  inhabitants = {
    "humans" : [],
    "robots" : []
  }
  #defining an instance
  def __init__(self, name = "Planet"):
    self.name = name
  #defining instance methods
  def add_human(self, human):
<<<<<<< HEAD
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
=======
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
>>>>>>> 725d7701e905c04d9678c9591772f140a373f274
