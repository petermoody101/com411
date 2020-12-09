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


human = Human()
human.display()

  