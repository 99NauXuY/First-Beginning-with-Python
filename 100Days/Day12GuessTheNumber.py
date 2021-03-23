import random

#Variablen
logo = '''
  ________                                __  .__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ 
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/             \/     \/          \/            \/    \/     \/       
'''

#Methoden
def guess(correct, attempt):
    '''Aske Number and Check it'''
    print(f'You have {attempt} attempts remaining to guess the number.')
    try:
        yourguessnumber = int(input("Make a guess:"))
        if yourguessnumber < correct:
            print("Too low.")
            print("Guess again.")
            return False
        elif yourguessnumber > correct:
            print("Too high.")
            print("Guess again.")
            return False
        else:
            print(f"You got it! The answer was {correct}.")
            print("Guess again.")
            return True
    except ValueError as e:
        print("Not a Number.")
        return False

def game():
    '''Startet das Spiel'''
    repeat = True
    attempt = 10
    #Spiel
    while repeat:
        NUMBER = random.randint(1, 100)
        print(logo)
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100")
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level == "hard":
            attempt = 5
        elif level != "easy":
            print("You didn't choose a difficulty. It's automatic easy.")
        while attempt != 0:
            right = guess(NUMBER, attempt)
            if right:
                attempt = 0
            else:
                attempt -= 1
                if attempt == 0:
                    print(f"You've run out of guesses, you lose. The answer was {NUMBER}.")
        again = input("This game has ended, run again? 'y' or 'n'.")
        if again != "y":
            repeat = False

game()
