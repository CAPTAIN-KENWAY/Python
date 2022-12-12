from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
from os import system

#item=MenuItem()
menu=Menu()
coffee=CoffeeMaker()
money=MoneyMachine()


choice=input(f"What would you like? ({menu.get_items()}): ").lower()