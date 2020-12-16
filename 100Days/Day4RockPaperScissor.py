import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
moeglichkeiten = [rock, paper, scissors]
while True:
    computerchoice = moeglichkeiten[random.randint(0,2)]
    while True:
        choice = input("What do you choose? " + \
                       "Type 0 for Rock, 1 for Paper or 2 for Scissor.\n")
        if int(choice) == 0 or int(choice) == 1 or int(choice) == 2:
            break
        else:
            print("falsche Eingabe!!!")
    choicestr = moeglichkeiten[int(choice)]
    print(choicestr)
    print("Computer choose:")
    print(computerchoice)
    if  (computerchoice == rock and choicestr == scissors) or \
        (computerchoice == scissors and choicestr == paper)or \
        (computerchoice == paper and choicestr == rock):
        print("You lose.")
        if input('Do you want to repeat(y/n)') == 'n':
            break
    elif computerchoice == choicestr:
        print("Its a draw")
        if input('Do you want to repeat(y/n)') == 'n':
            break
    else:
        print("You win.")
        if input('Do you want to repeat(y/n)') == 'n':
            break
