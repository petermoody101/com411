<<<<<<< HEAD
import random
from OOP.planet import Planet
from OOP.human import Human
from OOP.robot import Robot
class Universe:
  planets = []
  def __init__(self, name = "Universe"):
    self.name = name

  def generate(self):
    f = open("OOP/PlanetNames.txt", "r")
    lines = f.readlines()
    planetName = lines[random.randint(0, 19)]
    print(planetName)
    self.newPlanet = Planet(planetName)
    HumanPop = random.randint(1, 100)
    print(HumanPop)
    RobotPop = random.randint(1, 50)
    print(RobotPop)
    f2 = open("OOP/FirstNames.txt", "r")
    lines2 = f2.readlines()
    f3 = open("OOP/LastNames.txt", "r")
    lines3 = f3.readlines()
    for count in range(0, HumanPop, 1):
      humanName = str(lines2[random.randint(0, 10536)]) + " " + str(lines3[random.randint(0, 32408)])
      human = Human(humanName)
      Planet.add_human(self, human)
    
    for count in range(0, RobotPop, 1):
      robotName = lines2[random.randint(0, 10536)] + f"{random.randint(1000, 9999)}"
      robot = Robot(robotName)
      Planet.add_robot(self, robot)
    Universe.planets.append(self.newPlanet)

  def __repr__(self):
    return(f"The Universe contains the following planets {universe.planets}")

  def __str__(self):
    return(f"The Universe contains the planets, {universe.planets}")
#creating objects
universe = Universe()  
universe.generate()
print(universe.__str__())
print(Planet.__str__(universe.newPlanet))


    


  
=======
from random import random
from OOP.planet import planet
class universe:
  planets = []
  
  
  
>>>>>>> 725d7701e905c04d9678c9591772f140a373f274
