import random

global player_score
player_score = 0

global computer_score
computer_score = 0

global options
options = ["rock", "paper", "scissors"]


print("Rock Paper Scissors!\n")

play = input("Would you like to play? Y/N: ")

if play == "n" or play =="N":
    print("Goodbye.\n")
    quit()

while True:
    choice = input("\nChoose rock, paper, or scissors: ")
    decision = random.choice(options)

    print("\nRock!")
    print("Paper!")
    print("Scissors!")
    print("GO!\n")

    if choice != "rock" and choice != "paper" and choice != "scissors":
        print("Invalid input.\n")
        break

    if choice == "rock" and decision == "rock":
        print("It's a tie!")
        print("Current scores: Player with ", player_score, " wins and Computer with ", computer_score, "wins.\n")

    elif choice == "rock" and decision == "paper":
        print("You lost... :c")
        computer_score = computer_score + 1
        print("Current scores: Player with ", player_score, " wins and Computer with ", computer_score, "wins.\n")

    elif choice == "rock" and decision == "scissors":
        print("You won!!!")
        player_score = player_score + 1
        print("Current scores: Player with ", player_score, " wins and Computer with ", computer_score, "wins.\n")

    elif choice == "paper" and decision == "rock":
        print("You won!!!")
        player_score = player_score + 1
        print("Current scores: Player with ", player_score, " wins and Computer with ", computer_score, "wins.\n")

    elif choice == "paper" and decision == "paper":
        print("It's a tie!")
        print("Current scores: Player with ", player_score, " wins and Computer with ", computer_score, "wins.\n")

    elif choice == "paper" and decision == "scissors":
        print("You lost... :c")
        computer_score = computer_score + 1
        print("Current scores: Player with ", player_score, " wins and Computer with ", computer_score, "wins.\n")

    elif choice == "scissors" and decision == "rock":
        print("You lost... :c")
        computer_score = computer_score + 1
        print("Current scores: Player with ", player_score, " wins and Computer with ", computer_score, "wins.\n")

    elif choice == "scissors" and decision == "paper":
        print("You won!!!")
        player_score = player_score + 1
        print("Current scores: Player with ", player_score, " wins and Computer with ", computer_score, "wins.\n")

    elif choice == "scissors" and decision == "scissors":
        print("It's a tie!")
        print("Current scores: Player with ", player_score, " wins and Computer with ", computer_score, "wins.\n")

    play = input("Play again? Y/N: ")

    if play == "n" or play =="N":
        print("...\n...\n...")
        print("Goodbye.\n")
        break