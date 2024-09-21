import random
title = "Wecome to Rock Paper Scissors Game !"
width = 100
print("_"*width)
print(title.center(width))
print("_"*width)
print()
print()
while True :
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = ""
    while player not in choices:
        player = input("Enter a choice (rock , paper , scissors) : ").lower()

    if player == computer :
        print(f"Player : {player}")
        print(f"Computer : {computer}")
        print()
        print("Tie! ^_~")

    elif player == "rock" :
        if computer == "paper" :
            print(f"Player : {player}")
            print(f"Computer : {computer}")
            print()
            print("You lose! ~_~")

        if computer == "scissors" :
            print(f"Player : {player}")
            print(f"Computer : {computer}")
            print()
            print("You win! ^_^")

    elif player == "paper" :
        if computer == "rock" :
            print(f"Player : {player}")
            print(f"Computer : {computer}")
            print()
            print("You win! ^_^")

        if computer == "scissors" :
            print(f"Player : {player}")
            print(f"Computer : {computer}")
            print()
            print("You lose! ~_~")

    elif player == "scissors" :
        if computer == "rock" :
            print(f"Player : {player}")
            print(f"Computer : {computer}")
            print()
            print("you lose! ~_~")

        if computer == "paper" :
            print(f"Player : {player}")
            print(f"computer : {computer}")
            print()
            print("You win! ^_^")

    print()
    play_again = input("Wanna Play again (yes/no) :").lower()

    if play_again != "yes" :
        break
print("Thanks for Playing ! \n Bye ^.^")
