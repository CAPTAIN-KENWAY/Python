from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
from os import system

#item=MenuItem()
menu=Menu()
coffee=CoffeeMaker()
money=MoneyMachine()

while True:
    system('CLS')
    print(logo)
    choice=input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice=='off':
        print("Have a nice day.")
        break
    elif choice=='report':
        print(coffee.report())
        print(money.report())
        input()
    elif choice in ('espresso','latte','cappuccino'):
        print(coffee.is_resource_sufficient(menu.find_drink(choice)))
        # if coffee.is_resource_sufficient(menu.find_drink(choice))==True:
        #     if money.make_payment(menu.find_drink(choice).cost)==True:
        #         coffee.make_coffee(menu.find_drink(choice))
        input()               
    else:
        print("Invalid choice.")
        input()
