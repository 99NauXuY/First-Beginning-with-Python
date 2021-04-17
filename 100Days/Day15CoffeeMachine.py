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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(eingabe):
    not_enough = 0
    for zutaten in MENU[eingabe]['ingredients']:
        if resources[zutaten] < MENU[eingabe]['ingredients'][zutaten]:
            not_enough += 1
            print(f"Sorry there is not enough {zutaten}.")
    if not_enough > 0:
        return False
    else:
        return True


def check_coins(eingabe):
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))
    sum = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    if sum < MENU[eingabe]['cost']:
        print("Sorry that's not enough money. Money refund.")
        return False
    else:
        change = round(sum - MENU[eingabe]['cost'], 2)
        print(f"Here is ${change} dollars in change.")
        return True

#Kaffeemaschine
while True:
    choice = input("What would you iike? (espresso/latte/cappuccino):")
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if check_resources(choice):
            if check_coins(choice):
                for a in MENU[choice]['ingredients']:
                    resources[a] -= MENU[choice]['ingredients'][a]
                profit += round(MENU[choice]['cost'], 2)
                print(f"Here is your {choice}. Enjoy.")
    elif choice == "report":
        print(f" Water: {resources['water']}ml")
        print(f" Milk: {resources['milk']}ml")
        print(f" Coffee: {resources['coffee']}g")
        print(f" Money: ${profit}")
    elif choice == "off":
        break
    else:
        print("Ungueltige Eingabe.")