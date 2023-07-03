from data import *


def drink():                            # function for ordering a drink.
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    # for
    return choice

def check(current_menu):                # function for checking if there are enough resources.l
    validate_resources = True           # this vaiable is the one that will tell us if there are resources or not.
    for i in current_menu:              # the program goes through the dictionary with the menu and the ingredients
        if i == "ingredients":          # and compare if our resources are enough or not.
            for j in current_menu[i]:
                if current_menu[i][j] > resources[j]:
                    print(f"Sorry there is not enough {j}")
                    validate_resources = False
                else:
                    resources[j] = resources[j] - current_menu[i][j]
    return resources, validate_resources

def payment(total, current_menu):
    validate_money = True
    for i in current_menu:
        if i == "cost":
            if current_menu[i] > total:
                print("Sorry that's not enough money. Money refunded.")
                validate_money = False
            else:
                exchange = total - current_menu[i]
                total = current_menu[i]

    return validate_money, total, exchange

mode = True
money = 0
while mode:
    choice = drink()
    if choice == "off":
        print("Turning off machine")
        mode = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffe: {resources['coffee']}g")
        print(f"Money: {money}€")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        current_menu = MENU[choice]
        resources, validate_resources = check(current_menu)
        if validate_resources:
            print("Please insert coins.")
            fifty_cent = int(input("How many coins of fifty cent?: "))
            twenty_cent = int(input("How many coins of twenty cent?: "))
            ten_cent = int(input("How many coins of ten cent?: "))
            five_cent = int(input("How many coins of five cent?: "))
            total = round(fifty_cent*0.5+twenty_cent*0.2+ten_cent*0.1+five_cent*0.05, 2)
            validate_money, total, exchange = payment(total, current_menu)
            if validate_money:
                money += total
                print(f"Here is {exchange}€ in change.")
                print(f"Here is your {choice}")
    else:
        print("Sorry option not available")

