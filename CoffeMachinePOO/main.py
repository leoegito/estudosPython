"""
Basic POO exercise, using the given classes from the repository: coffe_maker, 
menu and money_machine.
"""
from menu import Menu, MenuItem
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()
is_on = True

money_machine.report()
coffe_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What drink would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink and coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)
