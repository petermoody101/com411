#defining a class
class robot:
  #defining class attributes
  laws = "Protect, Obey and Survive"
  MAX_ENERGY = 100
  #Defining a static method
  def the_laws():
    print(robot.laws)
  #defining a class method
  def assemble(cls):
    return cls("Assembled Robot")
  #defining initialiser 
  def __init__(self, name = "Robot", energy = 0):
    #assigning instance attributes
    self.name = name
    self.age = 0
    self.energy = robot.MAX_ENERGY
  #defining an instance method
  def display(self):
    print(f"I am {self.name}")
  #defining a formal string method
  def __repr__(self):
    return f"Robot(name={self.name}, age={self.age})"
  #defining an informal string method
  def __str__(self):
    return f"Robot {self.name}, is {self.age} years old."
  #defining grow method
  def grow(self):
    self.age = self.age + 1
  #defining eat method
  def eat(self, amount):
    #if statement to ensure energy does not exceed max energy
    if self.energy == robot.MAX_ENERGY:
      print ("Energy full, no need to eat")
    else:
      self.energy = self.energy + amount
  #defining move method
  def move(self, distance):
    #if statement to ensure energy does not fall lower than 0
    if self.energy != 0:
      self.energy = self.energy - distance
    else:
      print("No energy left, cannot move")


  
