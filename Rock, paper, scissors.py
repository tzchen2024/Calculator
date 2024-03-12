#Setup: Start by importing the random module.Create variables exit, user_points, and computer_points, and set exit to False, user_points and computer_points to 0.
import random 
exit = "False"
user_points = 0
computer_points = 0
#Main Loop:Create a while loop that continues until exit becomes True. 
while exit == "False":
  #Inside the loop: Create a list called options with the values "rock," "paper," and "scissors." 
  options = "rock", "paper", "scissors"
  #Use input() to ask the user to choose "rock," "paper," "scissors," or to exit. Store the user's input in a variable called user_input.
  user_input = input("rock, paper, scissors, or exit: ")
  #Generate a random choice for the computer from the options list and store it in a variable called computer_input.
  computer_input = random.choice(options)
  #If the user_input is "exit," print the game ending message, including the total scores, and set exit to True to exit the loop.
  if user_input == "exit":
    print("Game End ")
    print("You won a total of ", str(user_points), "and computer won a total of ", str(computer_points))
    exit = True
  if user_input == "rock":
    if computer_input == "rock":
      print("You chose rock")
      print("Computer chose rock")
      print("Tie")
    elif computer_input == "paper":
      print("You chose rock")
      print("Computer chose paper")
      print("Computer Wins")
      computer_points += 1
    elif computer_input == "scissors":
      print("You chose rock")
      print("Computer chose scissors")
      print("You Win")
      user_points += 1

  elif user_input == "paper":
    if computer_input == "paper":
      print("You chose paper")
      print("Computer chose paper")
      print("Tie")
    elif computer_input == "rock":
      print("You chose paper")
      print("Computer chose rock")
      print("You Win")
      user_points += 1    
    elif computer_input == "scissors":
      print("You chose paper")
      print("Computer chose scissors")
      print("Computer Win")
      computer_points += 1
      
  if user_input == "scissors":
    if computer_input == "rock":
      print("You chose scissors")
      print("Computer chose rock")
      print("Computer Wins")
      computer_points += 1
    elif computer_input == "paper":
      print("You chose scissors")
      print("Computer chose paper")
      print("You Win")
      user_points += 1  
    elif computer_input == "scissors":
      print("You chose scissors")
      print("Computer chose scissors")
      print("Tie")
  #If the user_input doesn't match any valid options ("rock," "paper," "scissors"), display an "Invalid Input" message.
  elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
    print("invalid input")
      