from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []


def deal_card():
    return random.choice(cards)


def calculate_score(l):
    if sum(l) == 21:
        return 0
    elif sum(l) > 21:
        if 11 in l:
            if sum(l)-11+1 > 21:
                return 1
            else:
                l[l.index(11)] = 1
                return 2
        else:
            return 1


def display():
    print(
        f"    Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(
        f"    Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")


def compare(player_score, computer_score):

    if computer_score == 21 and player_score == 21:
        display()
        print("You lose. 😤")
    elif computer_score > 21:
        display()
        print("Opponent went over. You win. 😁")
    elif player_score > 21:
        display()
        print("You went over. You lose. 😭")
    elif player_score > computer_score or player_score == 21:
        display()
        print("You win. 😁")
    elif player_score < computer_score or computer_score == 21:
        display()
        print("You lose. 😤")
    else:
        display()
        print("It's a Draw. ")


def play():
    player_cards.append(deal_card())
    computer_cards.append(deal_card())
    ans = 'y'
    while ans == 'y':
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
        if calculate_score(player_cards) == 0:
            display()
            print("You win with a Blackjack. 😎")
            break
        elif calculate_score(computer_cards) == 0:
            display()
            print("You lose. Opponent has a Blackjack 😱")
            break
        elif calculate_score(player_cards) == 1:
            display()
            print("You went over. You lose. 😭")
            break
        elif calculate_score(computer_cards) == 1:
            display()
            print("Opponent went over. You win. 😁")
            break
        print(
            f"Your cards: {player_cards}, current score: {sum(player_cards)}.")
        print(f"Computer's first card: {computer_cards[0]}")
        ans = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if ans == 'n':
            while sum(computer_cards) < 17:
                computer_cards.append(deal_card())
            if calculate_score(computer_cards) == 1:
                display()
                print("Opponent went over. You win. 😁")
                break
            else:
                compare(sum(player_cards), sum(computer_cards))


choice = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while choice == 'y':
    print(logo)
    player_cards = []
    computer_cards = []
    play()
    choice = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
