import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess!= random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess < random_number:
            print("Too low!")
            
        elif guess > random_number:
            print("Too high!")
    
    print("You got it!")



def compute_guess(x):
    low = 1 
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
         guess = random.randint(low, high)
        else:
            guess = low
        feeedback = input(f" Is {guess} to high? (H), too low (L), or correct? (C)").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"The Computer Has guessed your number {guess}! Correctly!")

# Change "guess(100" to play the computer guesses or you guesses.
guess(100)



    




    

