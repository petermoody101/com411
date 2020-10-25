#defining the function directions
def directions():
    #asking user to input number of items to add to list
    num_items = int(input("How many items to be added to the list? \n"))
    #creating list
    directions2 = []
    #for loop to iteratively append to the list
    for count in range(0, num_items, 1):
        #appending user input to the list
        directions2.append(input("Please enter the direction to be added to the list: \n"))
    #returning the list from the function
    return directions2

#defining the run function
def run():
    #printing the result of the directions function
    print (directions())
    
run()