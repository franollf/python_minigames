
import random



p1_wins = 0
p2_wins = 0


print("This is a Two Player Game")

p1_name = input("\nPlayer 1: What is your name? ")
p2_name = input("\nPlayer 2: What is your name? ")

input("\nPress Enter to Play!")


for _ in range(5):
     
     p1_roll = random.randint(1,6)
     p2_roll = random.randint(1,6)

     print(f"\n{p1_name} rolls {p1_roll}")
     print(f"{p2_name} rolls {p2_roll}")

     if p1_roll > p2_roll:
        print("\nPlayer 1 Wins!")
        p1_wins += 1
    
     if p2_roll > p1_roll:
        print("\nPlayer 2 Wins!")
        p2_wins += 1

     elif p2_roll == p1_roll: 
        print("\nIt was a tie!")

     input("Press Enter to Continue")

  
if p1_wins > p2_wins:
    print(f"\n{p1_name} Wins by {p1_wins - p2_wins} win!")

if p1_wins < p2_wins:
    print(f"\n{p2_name} Wins by {p2_wins - p1_wins}!")

if p1_wins == p2_wins:
    print(f"\n It was a tie! Nobody Wins!")
    








   
