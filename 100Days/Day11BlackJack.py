import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
#Variablen
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Methoden
def deal_card():
    '''Returns a random card.'''
    return cards[random.randint(0, len(cards)-1)]
def replay():
    replayvar = input("Another round? 'y' or 'n'?")
    if replayvar == 'y':
        return False
    else:
        return True
def score(myscore, npcscore):
    if (npcscore>21 and myscore <= 21) or (myscore > npcscore and myscore <= 21):
        return "You win."
    elif myscore == npcscore:
        return "Its a draw."
    else:
        return "You lose."
#Spiel
print(logo)
game_not_dead = True
while game_not_dead:
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    print(f'Deine Karten: {user_cards}, Score: {sum(user_cards)}')
    print(f'NPC erste Karte: {computer_cards[0]}')
    #blackjack
    if sum(computer_cards) == 21:
        print("Blackjack. You lose")
        if replay():
            game_not_dead = False
    elif sum(user_cards) == 21:
        print("Blackjack. You win")
        if replay():
            game_not_dead = False
    #ziehen
    else:
        #myturn
        loop = True
        while loop:
            choice = input("Type 'y' to get another card, type 'n' to pass:")
            if choice == "y":
                addcard = deal_card()
                if addcard == 11:
                    user_cards.append(1)
                    print(f'Deine Karten {user_cards}')
                else:
                    user_cards.append(addcard)
                    print(f'Deine Karten {user_cards}')
                if(sum(user_cards)) > 21:
                    print("Your sum is over 21")
                    loop = False
            else:
                loop = False
        #npcturn
        while sum(computer_cards) < 17:
            addcard2 = deal_card()
            if addcard2 == 11:
                computer_cards.append(1)
            else:
                computer_cards.append(addcard2)
        #ende
        print(f'Deine finale Karten: {user_cards}, final score: {sum(user_cards)}')
        print(f'NPC finale Karten: {computer_cards}, final score: {sum(computer_cards)}')
        print(score(sum(user_cards), sum(computer_cards)))
        if replay():
            game_not_dead = False
