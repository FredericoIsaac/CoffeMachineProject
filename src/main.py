# Imports
from coffe_data import MENU, resources


def print_report():
    """
    Print existing resources in the machine and current money
    """
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money_in_machine}")


def enough_resources(chosen_drink):
    """
    :return: A list with an resource if it was not enough of them, returns empty if enough resources
    """
    for key, values in chosen_drink["ingredients"].items():
        if resources[key] - values < 0:
            return [key]

    return []


def calculate_monetary_value(coin_quarters, coin_dimes, coin_nickles, coin_pennies):
    """
    :param coin_quarters: How much quarters coins the user introduce
    :param coin_dimes: How much dimes coins the user introduce
    :param coin_nickles: How much nickles coins the user introduce
    :param coin_pennies: How much pennies coins the user introduce
    :return: The value of money that the user introduce in the machine
    """
    return monetary_coins_value["quarters"] * coin_quarters + monetary_coins_value["dimes"] * coin_dimes + monetary_coins_value["nickles"] * coin_nickles + monetary_coins_value["pennies"] * coin_pennies


def deducted_resources(chosen_drink):
    """
    Change resources to subtract drink resources
    :param chosen_drink: The drink chosen
    """
    for key, values in chosen_drink["ingredients"].items():
        resources[key] -= values


money_in_machine = 0

monetary_coins_value = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

while True:
    menu_choice = input("    What would you like? (espresso/latte/cappuccino): ")

    if menu_choice == "off":
        break
    elif menu_choice == "report":
        print_report()
    else:
        drink = MENU[menu_choice]

        drink_resource = enough_resources(drink)

        if drink_resource:
            print(f"    Sorry there is not enough {drink_resource[0]}.")
        else:
            print("Please insert coins.")
            quarters = float(input("how many quarters?: "))
            dimes = float(input("how many dimes?: "))
            nickles = float(input("how many nickles?: "))
            pennies = float(input("how many pennies?: "))

            money_inserted = calculate_monetary_value(quarters, dimes, nickles, pennies)
            cost_of_drink = drink["cost"]

            if money_inserted < cost_of_drink:
                print("Sorry that's not enough money. Money refunded.")
            elif money_inserted >= cost_of_drink:
                money_in_machine += cost_of_drink
                change = money_inserted - cost_of_drink
                print("Here is ${:.2f} in change.".format(change))

                deducted_resources(drink)
                print(f"Here is your {menu_choice} ☕ Enjoy!")


