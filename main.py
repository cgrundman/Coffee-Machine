# COFFEE MACHINE

#  Definition of Menu
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

# Resources initially in machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

cont = True


# Function to input money
def money_input(variable):
    quarters = int(input("How many quarters do you have? "))
    dimes = int(input("How many dimes do you have? "))
    nickels = int(input("How many nickels do you have? "))
    pennies = int(input("How many pennies do you have? "))
    money_in = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    cost_def = MENU[variable]
    price = cost_def["cost"]
    if price > money_in:
        print("Sorry not enough money. Money returned.")
        return False
    else:
        change = money_in - price
        print(f"Your change is ${change}")
        return True


# Function to retrieve the water for recipe.
def pull_water():
    order_recipe = MENU[start]
    order_ingredients = order_recipe['ingredients']
    order_water = order_ingredients['water']
    return order_water


# Function to retrieve the coffee for recipe.
def pull_coffee():
    order_recipe = MENU[start]
    order_ingredients = order_recipe['ingredients']
    order_coffee = order_ingredients['coffee']
    return order_coffee


# Function to retrieve the milk for recipe.
def pull_milk():
    order_recipe = MENU[start]
    order_ingredients = order_recipe['ingredients']
    order_milk = order_ingredients['milk']
    return order_milk


# Function to retrieve the cost.
def pull_cost():
    order_recipe = MENU[start]
    order_cost = order_recipe['cost']
    return order_cost


def not_enough(variable):
    print(f" Sorry, not enough {variable}.")


# Continue loop
while cont is True:

    # Order Selection
    start = input("What you would like? (espresso/latte/cappuccino)  ")

    # Report on resources in machine currently
    if start == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")

    # Espresso Order
    if start == "espresso":
        money_condition = money_input(start)
        if money_condition is True:
            water = pull_water()
            if water <= resources['water']:
                resources['water'] -= water
            else:
                not_enough("water")
            coffee = pull_coffee()
            if coffee <= resources['coffee']:
                resources['coffee'] -= coffee
            else:
                not_enough("coffee")
            if coffee <= resources['coffee'] and water <= resources['water']:
                print("Thank you for your order, please come again!")

    # Latte Order
    if start == "latte":
        money_condition = money_input(start)
        if money_condition is True:
            water = pull_water()
            if water <= resources['water']:
                resources['water'] -= water
            else:
                not_enough("water")
            coffee = pull_coffee()
            if coffee <= resources['coffee']:
                resources['coffee'] -= coffee
            else:
                not_enough("coffee")
            milk = pull_milk()
            if milk <= resources['milk']:
                resources['milk'] -= milk
            else:
                not_enough("milk")
            if milk <= resources['milk'] and coffee <= resources['coffee'] and water <= resources['water']:
                print("Thank you for your order, please come again!")


    # Cappuccino Order
    if start == "cappuccino":
        money_condition = money_input(start)
        if money_condition is True:
            water = pull_water()
            if water <= resources['water']:
                resources['water'] -= water
            else:
                not_enough("water")
            coffee = pull_coffee()
            if coffee <= resources['coffee']:
                resources['coffee'] -= coffee
            else:
                not_enough("coffee")
            milk = pull_milk()
            if milk <= resources['milk']:
                resources['milk'] -= milk
            else:
                not_enough("milk")
            if milk <= resources['milk'] and coffee <= resources['coffee'] and water <= resources['water']:
                print("Thank you for your order, please come again!")
