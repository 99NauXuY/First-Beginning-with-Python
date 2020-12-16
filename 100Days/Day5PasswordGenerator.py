#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
countletters =len(letters) - 1
countsymbols =len(symbols) - 1
countnumbers =len(numbers) - 1
print("Welcome to the PyPassword Generator!")
level = int(input("Type 0 for easy Password and 1 for hard Password.\n"))
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ''
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for letter in range(1,nr_letters+1):
    password += letters[random.randint(0,countletters)]
for symbol in range(1,nr_symbols+1):
    password += symbols[random.randint(0,countsymbols)]
for number in range(1,nr_numbers+1):
    password += numbers[random.randint(0,countnumbers)]
if level ==0:
    print(f"Here is your easy Password: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
elif level == 1:
    hardpassword = []
    newpassword = ""
    for character in password:
        hardpassword.append(character)
    random.shuffle(hardpassword)
    for a in hardpassword:
        newpassword += a
    print(f"Here is your hard Password: {newpassword}")
else:
    "Falsche Eingabe!"
