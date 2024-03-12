import string
import random
#Import the string and random modules. These modules provide functions to work with strings and generate random values.
characters = list(string.ascii_letters + string.digits + " !@#$%^&*()") #Create a list of characters to use for generating the password. This includes letters (both uppercase and lowercase), digits, and some special characters.
def generate_password():
  password_length = int(input("How long would you like your password to be? "))
  #Ask the user for the desired length of the password.
  random.shuffle(characters)
  #Shuffle the characters to randomize their order.
  password = []
  #Create an empty list called password.
  for x in range(password_length):
    #Choose a random character from the shuffled list of characters and append it to the password list.
    password.append(random.choice(characters)) 
  random.shuffle(password)
    #Shuffle the password list to mix up the characters.
  password = "" .join(password)
    #Join the characters in the password list into a single string.
  print(password)

option = input("Do you want to generate a password (Yes/No).")

if option == "Yes":
  generate_password()
elif option == "No":
  print("Program ended")
  quit()
  #If the user selects "No," print "Program ended" and exit the program.
else: #If the user inputs anything other than "Yes" or "No," print "Invalid input, please input Yes or No" and exit the program.
  print("Invalid input, please input Yes or No")
  quit()
  


