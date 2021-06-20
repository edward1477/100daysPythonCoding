
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
}

resourcesKeyList = list(resources.keys())
amount_quarters = 0.25
amount_dimes = 0.1
amount_nickles = 0.05
amount_pennies = 0.01
profit = 0


def print_report():
    print(f"{resourcesKeyList[0]}: {resources['water']}ml")
    print(f"{resourcesKeyList[1]}: {resources['milk']}ml")
    print(f"{resourcesKeyList[2]}: {resources['coffee']}g")
    print(f"money: ${profit}")


def is_enough_resources(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""

    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * amount_quarters
    total += int(input("How many dimes?: ")) * amount_dimes
    total += int(input("How many nickles?: ")) * amount_nickles
    total += int(input("How many pennies?: ")) * amount_pennies
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""

    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change != 0:
            print(f"Here is ${change} dollars in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, ingredients):
    """Deduct the required ingredients from the resources."""

    for item in resources:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


# TODO 1: Prompt user "What would you like? (espresso/latte/cappuccino)
is_ON = True
while is_ON:
    userInput = input("What would you like? (espresso/latte/cappuccino): ")

# TODO 2: Check user input, if "off" -> end the program
    if userInput == "off":
        is_ON = False

# TODO 3: If "report" -> print current resources report
    elif userInput == "report":
        print_report()

# TODO 4: If "drink"
# check enough resources
    else:
        drink = MENU[userInput]
        if is_enough_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(userInput, drink["ingredients"])
