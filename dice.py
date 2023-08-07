import random

p1_wins = 0
p2_wins = 0

for i in range(10):

    p1_roll = random.randint(1,6)
    p2_roll = random.randint(1,6)

    print(f'Player 1 rolls: {p1_roll}')
    print(f'PLayer 2 rolls: {p2_roll}')

    if p1_roll > p2_roll:
        print ('Player 1 Wins!')
        p1_wins += 1
        

    if p1_roll < p2_roll:
        print ('Player 2 Wins!')
        p2_wins += 1
        

    if p1_roll == p2_roll:
        print ('Draw!')
        

    input('Press Enter To Continue:')


print("Game over!")
if p1_wins > p2_wins:
    print(f'Player 1 Wins! {p1_wins}' ' points')

if p2_wins > p1_wins:
    print(f'Player 2 Wins!{p2_wins}' 'points')  

        



   