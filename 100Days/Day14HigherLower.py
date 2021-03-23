import random
from Day14Data import data

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def compareprint(A, B):
    print(f"Compare A: {data[A]['name']}, {data[A]['description']},{data[A]['country']}.")
    print(vs)
    print(f"Against B: {data[B]['name']}, {data[B]['description']},{data[B]['country']}.")
    decision = input("Who has more followers? Type 'A' or 'B'.")
    if (decision == "A" and data[A]['follower_count'] > data[B]['follower_count']) or \
            (decision == "B" and data[A]['follower_count'] < data[B]['follower_count']):
        return True
    else:
        return False


# Spiel
def game():
    score = 0
    A = random.randint(0, len(data) - 1)
    game_not_dead = True
    print(logo)
    while game_not_dead:
        B = random.randint(0, len(data) - 1)
        if compareprint(A, B):
            score += 1
            A = B
            print(f'You are right! Current Score: {score}.')
        else:
            print(f'Sorry thats wrong. Final Score: {score}.')
            game_not_dead = False


game()
