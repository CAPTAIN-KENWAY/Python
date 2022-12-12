from art import logo, vs
from os import system
from game_data import data
import random
player_score = 0
system('CLS')
print(logo)

choice1 = random.choice(data)
while True:
    choice2 = random.choice(data)
    print(
        f"Compare A: {choice1['name']}, {choice1['description']}, from {choice1['country']}")
    print(vs)
    print(
        f"Against B: {choice2['name']}, {choice2['description']}, from {choice2['country']}")
    ans = input("Who has more followers? Type 'A' or 'B': ").upper()
    if ans == 'A':
        if choice1['follower_count'] > choice2['follower_count']:
            player_score += 1
            system('CLS')
            print(logo)
            print(f"You're right! Current score: {player_score}")
        else:
            system('CLS')
            print(logo)
            print(f"Sorry that's wrong. Final score: {player_score}")
            break
    elif ans == 'B':
        if choice2['follower_count'] > choice1['follower_count']:
            player_score += 1
            system('CLS')
            print(logo)
            print(f"You're right! Current score: {player_score}")
            choice1 = choice2
        else:
            system('CLS')
            print(logo)
            print(f"Sorry that's wrong. Final score: {player_score}")
            break
    else:
        system('CLS')
        print(logo)
        print(f"Invalid choice. Final score: {player_score}")
        break
