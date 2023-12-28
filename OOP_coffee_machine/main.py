from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_mchine = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What is your order going to be? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_mchine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_mchine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_mchine.make_coffee(drink)