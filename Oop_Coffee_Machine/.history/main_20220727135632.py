from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
from os import system

#item=MenuItem()
menu=Menu()
coffee=CoffeeMaker()
money=MoneyMachine()
print(coffee.report())
print(money.report())
'''
while True:
    system('CLS')
    print(logo)
    choice=input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice=='off':
        print("Have a nice day.")
        break
    elif choice=='report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        input()

'''