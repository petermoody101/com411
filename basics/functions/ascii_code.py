print("Program Started")
char1 = input("Please enter a standard character \n")
if len(char1) == 1:
  code1 = ord(char1)
  print ("The ascii code for {} is {}".format(char1, code1))
else:
  print("Please input a single character")

print("Program ended")