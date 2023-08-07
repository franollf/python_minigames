import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    if user_wins == 10:
        print("You have reached 10 wins first! Congrats!")
        quit()

    if computer_wins == 10:
        print("The Computer has reached 10 wins first! You Lose!")
        quit()

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You've Won! ")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You've Won! ")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == 'rock':
        print("You've Won! ")
        user_wins += 1

    elif user_input == "rock" and computer_pick == 'rock':
        print ('Its a tie! ')

    elif user_input == "paper" and computer_pick == 'paper':
        print ('Its a tie! ')

    elif user_input == "scissors" and computer_pick == 'scissors':
        print ('Its a tie!' )

    else:
        print("Youve Lost!")
        computer_wins += 1

if computer_wins > user_wins:
    print('You have lost to the CPU by ', str(computer_wins - user_wins), " Better Luck Next Time! You had ", str(user_wins) + "wins")
    quit()

if user_wins > computer_wins:
    print('You have won by ', str(user_wins - computer_wins), "Great Work! You had " + str(user_wins), "wins" )
    quit()

if user_wins == computer_wins:
    print ("Its a tie! You both had ",str(user_wins), "wins Better luck next time! ")
    quit()
    