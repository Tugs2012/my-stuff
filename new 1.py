import random

options = ["rock", "paper", "scissor"]
player = None
computer = random.choice(options)
while player not in options:
    player = input("Enter a choice (rock, paper, scissor):")
print(f"Player: {player}")
print(f"Computer: {computer}")
if player == computer:
	print("Tied!")
elif player == "rock" and computer == "scissor":
	print("you won!")
elif player == "paper" and computer == "rock":
	print("You won!")
elif player == "scissor" and computer == "paper":
	print("You won!")
else:
	print("You Lose!")