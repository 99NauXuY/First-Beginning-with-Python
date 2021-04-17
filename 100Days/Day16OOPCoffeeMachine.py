from Day16menu import Menu, MenuItem
from Day16coffee_maker import CoffeeMaker
from Day16money_machine import MoneyMachine

menu = Menu()
automat = CoffeeMaker()
geld_wechsler = MoneyMachine()

while True:
    choice = input(f"What would you iike? {menu.get_items()}:")
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if automat.is_resource_sufficient(menu.find_drink(choice)):
            if geld_wechsler.make_payment(menu.find_drink(choice).cost):
                automat.make_coffee(menu.find_drink(choice))
    elif choice == "report":
        automat.report()
        geld_wechsler.report()
    elif choice == "off":
        break
    else:
        print("Ungueltige Eingabe.")