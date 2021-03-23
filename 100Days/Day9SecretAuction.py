from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
daten = {}
print(logo)
print("Welcome to the secret auction program")
while True:
    name = input("What is your name?:")
    try:
        bid = int(input("What is your bid?: €"))
    except:
        bid = 0
    daten[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'.")
    clear()
    if choice == "no":
        break
maxBider = ""
maxBid = 0
for bids in daten:
    if daten[bids] > maxBid:
        maxBid = daten[bids]
        maxBider = bids
if maxBider == "":
    print("There is no winner.")
else:
    print(f'The winner is {maxBider} with a bid of €{maxBid}')
