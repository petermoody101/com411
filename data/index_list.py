#defining movements function
def movements():
  #defining path list
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  #returning list from function
  return path

#defining run function
def run():
  print ("Moving...")
  #storing return from movements function
  path2 = movements()
  #creating variables to be used when outputting directions 
  x = int(0)
  y = int(1)
  #for loop for half the length of the list
  for count in range(0, (int(len(path2)/2)), 1):
    #outputting directions
    print("{} for {} steps".format(path2[x],path2[y]))
    #increasing x and y variables to move along list when outputting
    x = x + 2
    y = y + 2

run()