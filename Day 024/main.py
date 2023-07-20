with open("./Input/Letters/starting_letter") as letter:
    letter = letter.read()
with open("./Input/Names/invited_names") as file_names:
    for i in file_names:
        with open(f"./Output/letter_for_{i.strip()}", "w") as final_letter:
            letter = letter.replace(letter.split()[1], i.strip())
            final_letter.write(letter)