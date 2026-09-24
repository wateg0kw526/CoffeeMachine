# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
# #print(MENU["espresso"]["ingredients"]["water"])
# money = 0
# coffee_choice = input("Welcome to the coffee kiosk!\n\nWhat would you like? (espresso/latte/cappuccino):\n" )
#
# print(resources)
#
# def make_coffee(drink_dict):
#     for item, amount in drink_dict["ingredients"].items():
#         resources[item] -= amount
#     return resources
#
# def money_collected(drink_dict):
#     for item, price in drink_dict["cost"].items():
#         resources[item] += money
#     return resources
#
# make_coffee(MENU[coffee_choice])
# money_collected(MENU[coffee_choice])
# print(resources)





MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5,},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0,},
}
resources = {"water": 300, "milk": 200, "coffee": 100}

money = 0

coffee_choice = input(
    "Welcome to the coffee kiosk!\n\nWhat would you like? (espresso/latte/cappuccino):\n"
)
print("Before:", resources)


def check_resources(drink_dict):
    """Check if enough resources are available."""
    for item, amount in drink_dict["ingredients"].items():
        if resources.get(item, 0) < amount:
            print(f"Sorry, not enough {item}.")
            return False
    return True


def make_coffee(drink_dict):
    for item, amount in drink_dict["ingredients"].items():
        resources[item] -= amount


def process_transaction(drink_dict):
    global money
    cost = drink_dict["cost"]
    money += cost
    print(f"Collected ${cost:.2f}. Total money: ${money:.2f}")



if check_resources(MENU[coffee_choice]):
    make_coffee(MENU[coffee_choice])
    process_transaction(MENU[coffee_choice])
    print("After resources:", resources)


