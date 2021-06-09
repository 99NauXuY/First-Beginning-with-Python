import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
formatted_data = {row.letter: row.code for (index, row) in data.iterrows()}


def generate():
    name = input("Enter a name:").upper()
    try:
        output_list = [formatted_data[letter] for letter in name]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        generate()
    else:
        print(output_list)


generate()
