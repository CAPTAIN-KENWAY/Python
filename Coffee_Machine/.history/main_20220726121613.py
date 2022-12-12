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

def process_coins(total,cost):    
    if total>cost:
        print(f"Here is ${round(total-cost,2)} in change.")
        return True
    elif total==cost:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffee(choice):
    pass

user_money=[0]*4

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
    elif choice in ('espresso','latte','cappuccino'):
        if check_resources(choice)==True:
            print("Please insert coins.")
            user_money[0]=(int(input("How many quarters?: ")))
            user_money[1]=(int(input("How many dimes?: ")))
            user_money[2]=(int(input("How many nickels?: ")))
            user_money[3]=(int(input("How many pennies?: ")))
            total=user_money[0]*0.25 + user_money[1]*0.1 + user_money[2]*0.05 +user_money[3]*0.01
            cost=float(MENU[choice]['cost'])
            if process_coins(total,cost)==True:
                print(f"Here is your {choice.title()} ☕. Enjoy!")
                if choice=='espresso':
                    resources["water"]=resources["water"]-MENU[choice]["ingredients"]["water"]
                    resources["coffee"]=resources["coffee"]-MENU[choice]["ingredients"]["coffee"]
                    resources["money"]+=cost
                else:
                    resources["water"]=resources["water"]-MENU[choice]["ingredients"]["water"]
                    resources["milk"]=resources["milk"]-MENU[choice]["ingredients"]["milk"]
                    resources["coffee"]=resources["coffee"]-MENU[choice]["ingredients"]["coffee"]
                    resources["money"]+=cost                  
    else:
        print("Invalid choice.")
        break



