from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_ON = True
while is_ON:
    userInput = input(f"What would you like? {menu.get_items()}: ")
    if userInput == "off":
        is_ON = False
    elif userInput == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(userInput)

        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

