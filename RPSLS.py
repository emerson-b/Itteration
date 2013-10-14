#rock paper scissors lizard spock
rock = "Rock"
spock = "Spock" 
lizard = "Lizard"
paper = "Paper"
scissors = "Scissors"




def game():
    if choice == "Rock" and opponent == scissors:
        win()
    elif choice == "Scissors" and opponent == paper:
        win()
    elif choice == "Paper" and opponent == lizard:
        win()
    elif choice == "Lizard" and opponent == spock:
        win()
    elif choice == "Spock" and opponent == rock:
        win()
    elif choice == "Rock" and opponent == rock:
        draw()
    elif choice == "Scissors" and opponent == scissors:
        draw()
    elif choice == "Paper" and opponent == paper:
        draw()
    elif choice == "lizard" and opponent == lizard:
        draw()
    elif choice == "Spock" and opponent == spock:
        draw()
    else:
        lose()
def win():
    print()
    print("Opponent choses {0}".format(opponent))
    print()
    print("Conratulations {0} beats {1}. You Win!".format(choice,opponent))
    playagain = False
def lose():
    print()
    print("Opponent choses {0}".format(opponent))
    print()
    print("Sorry {0} beats {1}. You Lose.".format(opponent,choice))
    playagain = False
def draw():
    print()
    print("Opponent choses {0}".format(opponent))
    print()
    print("Oh! Looks like its a draw as you both picked {0}. Try Again!".format(choice))
    
  
choice = input("Please enter your choice of Rock, Paper, Scissors, Lizard or Spock: ")
import random
opponent = random.choice([rock,spock,lizard,paper,scissors])
game()
    

    
    




