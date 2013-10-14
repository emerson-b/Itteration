#rock paper scissors lizard spock
rock = "Rock"
spock = "Spock" 
lizard = "Lizard"
paper = "Paper"
scissors = "Scissors"



def game():
    def win():
        print()
        print("Opponent choses {0}".format(opponent))
        print()
        print("Conratulations {0} beats {1}. You Win!".format(choice,opponent))
        print()
    def lose():
        print()
        print("Opponent choses {0}".format(opponent))
        print()
        print("Sorry {0} beats {1}. You Lose.".format(opponent,choice))
        print()
   
    def draw():
        print()
        print("Opponent choses {0}".format(opponent))
        print()
        print("Oh! Looks like its a draw as you both picked {0}. Try Again!".format(choice))
        print()
    choice = input("Please enter your choice of Rock, Paper, Scissors, Lizard or Spock: ")
    import random
    opponent = random.choice([rock,spock,lizard,paper,scissors])
    if choice == "Rock" and (opponent == scissors or opponent == lizard):
        win()
    elif choice == "Scissors" and (opponent == paper or opponent == lizard):
        win()
    elif choice == "Paper" and (opponent == lizard or opponent == spock):
        win()
    elif choice == "Lizard" and (opponent == spock or opponent == paper):
        win()
    elif choice == "Spock" and (opponent == rock or opponent == spock):
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
print("Welcome to Rock Paper Scissors Lizard Spock")
print("How to play:")
print("Rock crushes Scissors and Lizard")
print("Scissors cuts Paper and decapitates Lizard")
print("Paper covers Rock and disproves Spock")
print("Lizard poisons Spock and eats Paper")
print("Spock vaporizes Rock and smashes Scissors")
print()
play = "y"
while play == "y":
    play = input("Do you want to play (y/n): ")
    if play == "y":
        game()
    
  



    
    




