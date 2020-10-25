#defining directions function
def directions():
  #defining directions list
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  #returning list
  return directions

#defining menu function
def menu():
  print ("Please select a direction:\n")
  #storing return from function in local variable
  directions2 = directions()
  #for loop for length of local variable
  for count in range(0, len(directions2), 1):
    #outputting choices as formatted from list
    print ("{}:{} \n".format(count,directions2[count]))

#dedining run function
def run():
  #calling menu function
  menu()

run()
