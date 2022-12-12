MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}
def check_resources(choice):
    if MENU[choice]['ingredients']['water']>resources["water"]:
        print("Sorry not enough water.")
        return False
    elif choice!='espresso' and MENU[choice]['ingredients']['milk']>resources["milk"]:
        print("Sorry not enough milk.")
        return False
    elif MENU[choice]['ingredients']['coffee']>resources["coffee"]:
        print("Sorry not enough coffee.")
        return False
    else:
        return True

def process_coins(user_money):
    pass


user_money=[]

while True:
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=='off':
        print("Have a nice day.")
        break
    elif choice=='report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        break
    elif choice in ('espresso','latte','cappuccino'):
        if check_resources(choice=choice)==True:
            print("Please insert coins.")
            user_money.append(int(input("How many quarters?: ")))
            user_money.append(int(input("How many dimes?: ")))
            user_money.append(int(input("How many nickels?: ")))
            user_money.append(int(input("How many pennies?: ")))
            print(user_money)
            break
        else:
            break
    else:
        print("Invalid choice.")
        break



