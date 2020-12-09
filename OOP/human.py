#defining a class
class Human:
  #setting class attributes
  MAX_ENERGY = 100
  #defining an instance
  def __init__(self, name = "human", age = 0, energy = MAX_ENERGY):
    #assigning instance attributes
    self.name = name
    self.age = age
    self.energy = energy
  #defining a method
  def display(self):
    print(f"I am {self.name}")
  #defining a formal string method
  def __repr__(self):
    return f"Human(name = {self.name}, age = {self.age})"
  #defining an informal string method
  def __str__(self):
    return f"Human {self.name} is {self.age} years old."
  #defining grow method
  def grow(self):
    self.age = self.age + 1
  #defining eat method
  def eat(self, amount):
    #if statement to ensure energy does not exceed max energy
    if self.energy = MAX_ENERGY:
      print "Energy full, no need to eat"
    else:
      self.energy = self.energy + amount
  #defining move method
  def move(self, distance):
    #if statement to ensure energy does not fall lower than 0
    if self.energy != 0:
      self.energy = self.energy - distance
    else:
      print("No energy left, cannot move")



human = Human()
human.display()

  