from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine = True
maker = CoffeeMaker()
payment = MoneyMachine()
options = Menu()

while machine:
    order = input(f"What would you like? {options.get_items()}: ")
    if order == "report":
        maker.report()
        payment.report()
    elif order == "off":
        break
    else:
        drink = options.find_drink(order)
        enough_resources = maker.is_resource_sufficient(drink)
        enough_money = payment.make_payment(drink.cost)
        if enough_resources and enough_money:
            coffe = maker.make_coffee(drink)
        else:
            continue
