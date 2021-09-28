#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
# print(nato_df)
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def phonetic_alphabet():
    word = input("Enter a word: ").upper()
    try:
        word_nato = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        phonetic_alphabet()
    else:
        print(word_nato)

phonetic_alphabet()
