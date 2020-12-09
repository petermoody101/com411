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
    self.energy = energy
  #defining an instance method
  def display(self):
    print(f"I am {self.name}")
  #defining a formal string method
  def __repr__(self):
    return f"Robot(name={self.name}, age={self.age})
  #defining an informal string method
  def __str__(self):
    return f"Robot {self.name}, is {self.age} years old."


  
