import random

user = 0
computer = 0

options = ["rock", "paper", "scissor"]

while True:

    user_type = input("Type rock/paper/scissor").lower()

    if user_type ==  "exit":
        quit()

    if user_type not in options :
        continue

    random_number = random.randint(0,2)
    computer_type = options[random_number]

    print("computer", computer_type)

    if user_type == "rock" and computer_type == "scissor":
        print("You won")
        user += 1

    elif user_type == "paper" and computer_type == "rock":
        print("You won")
        user += 1

    elif user_type == "scissor" and computer_type == "paper":
        print("You won")
        user += 1

    else:
        print("You loss")
        computer += 1


    print("You won", user)
    print("Computer won", computer)
