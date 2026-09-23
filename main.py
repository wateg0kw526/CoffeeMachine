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

# TODO 1: Print report of all coffee machine resources.



# TODO 2. Get a logo, import it and print it.

from art import logo
print(logo)
#TODO 3. Print a greeting.

def make_coffee(drink_dict):
    for item, amount in drink_dict["ingredients"].items():
        resources[item] -= amount
    return resources

print(resources)

coffee_choice = input("Welcome to the coffee kiosk!\n\nWhat would you like? (espresso/latte/cappuccino):\n" )

make_coffee(MENU[coffee_choice])

print(resources)
#print(f"Espresso price is: $",MENU["espresso"]["cost"], "\nLatte price is: $",MENU["latte"]["cost"], "\nCappuccino price is: $",MENU["cappuccino"]["cost"])

