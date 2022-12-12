#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo
easy=10
hard=5
number=random.randint(1,101)
def check_guess(guess):
    if guess>number:
        return 1
    elif guess<number:
        return 2
    else:
        return 0
print(logo)
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty=='easy':
    attempts=easy
else: 
    attempts=hard

while True:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if check_guess(guess)==1:
        print("Too high.")
        attempts-=1
        if attempts==0:
            print("You've run out of guesses. You lose.")
            break
        print("Guess Again.")
    elif check_guess(guess)==2:
        print("Too low.")
        attempts-=1
        if attempts==0:
            print("You've run out of guesses. You lose.")
            break
        print("Guess Again.")
    else:
        print(f"You got it! The answer was {number}.")
        break

