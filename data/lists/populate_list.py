#defining directions function
def directions():
  #defining directions list
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  #returning list
  return directions

#defining menu function
def menu():
  print ("\nPlease select a direction:\n")
  #storing return from function in local variable
  directions2 = directions()
  #for loop for length of local variable
  for count in range(0, len(directions2), 1):
    #outputting choices as formatted from list
    print ("{}:{} \n".format(count,directions2[count]))
  #taking user input after displaying directions
  user_direction = input("")
  #checking that user input is an integer
  if user_direction.isdigit():
    user_direction = int(user_direction)
    move = directions2[user_direction]
  else:
    print("Please input the number corresponding to your desired direction. \n")
  return move

#dedining run function
def run():
  route = []
  print("Working out escape route...")
  for count in range(0, 5, 1):
    #calling menu function
    route.append(menu())
  print("Escape route: {} \n".format(route))

run()

