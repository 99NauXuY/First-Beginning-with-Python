import random

def blank(erratenewort):
    blankesWort = ""
    for buchstabe in erratenewort:
        blankesWort += "_"
    return blankesWort

def gewonnen(erratenewort):
    vorhanden = 0
    for buchstabe in erratenewort:
        if buchstabe == "_":
            vorhanden += 1
    if vorhanden == 0:
        return True
    else:
        return False

def swap(index, buchstabe, wort):
    liste = list(wort)
    liste[index] = buchstabe
    return "".join(liste)

word_list = ["kakao", "tee", "kaffee"]
versuche = 9
wort = word_list[random.randint(0, len(word_list)-1)]
unsichtbar = blank(wort)

while True:
    print(unsichtbar)
    choice = input("Gib ein Buchstabe ein: ")
    index = 0
    richtigzaehler = 0
    for a in wort:
        if a == choice:
            unsichtbar = swap(index, choice, unsichtbar)
            richtigzaehler += 1
        index += 1
    if gewonnen(unsichtbar):
        print("Du hast das Wort erraten. Glückwunsch!")
        break
    else:
        if richtigzaehler == 0:
            versuche -= 1
            if versuche == 0:
                print("Du hast verloren.")
                break
            print("noch " + str(versuche) + " Versuche")
