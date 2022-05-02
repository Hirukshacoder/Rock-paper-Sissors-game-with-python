import random
print("Welcome to python rock paper sissors game!!!!!")
tools = 'rock', 'paper', 'scissors'
players_tool = input("What do you choose [rock] [paper] [sissors]: ")
print("You chose",players_tool)
computer = random.choice(tools)
print("computer chose",computer)
if computer == 'rock' and players_tool == 'paper':
  print("You won")
if computer == 'paper' and players_tool == 'rock':
  print("You loose")
if computer == 'paper' and players_tool == 'sissors':
  print("You won")
if computer == 'sissors' and players_tool == 'paper':
  print("you loose")
if computer == 'rock' and players_tool == 'sissors':
  print("You loose")
if computer == 'sissors' and players_tool == 'rock':
  print("You won")
if computer == players_tool:
  print("Its a tie")

print("Thanks for playing")
