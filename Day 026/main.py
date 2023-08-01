import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_alphabet_DF = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {data.letter: data.code for (index, data) in nato_alphabet_DF.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("enter a word: ")
word_list = [i.upper() for i in word]
coded_list = [nato_alphabet_dict[i] for i in word_list]

print(coded_list)