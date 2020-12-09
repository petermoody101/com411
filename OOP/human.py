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


human = Human()
human.display()

  