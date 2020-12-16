print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
richtung = input('You are at a cross road.Where do you want to go ?Type "left" or "right".\n')

if richtung == "right":
    print("Fall into a hole. Game Over!")
elif richtung == "left":
    wahl1 = input('''You came to a lake. There is a island in the middle of the lake.
Type "wait" for a boat. Type "swim" to swim cross.\n''')
    if wahl1 == "wait":
        wahl2 = input("You arrive at the island unharmed."+
                " There is a house with 3 doors."+
                " Red, blue and yellow. Which color do you choose?\n")
        if wahl2 == "yellow":
            print("You Win!")
        elif wahl2 == "red":
            print("Burned by fire. Game over!")
        elif wahl2 == "blue":
            print("Eaten by beasts. Game over!")
        else:
            print("Game over!")
    else:
        print("Game over!")
else:
    print("Falsche Eingabe")
