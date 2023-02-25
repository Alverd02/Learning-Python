alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

play=True                 # Variable so the programs runs many times unless we change it

while play==True:         # Loop with the variable mentioned before

    mode = input("Type \"encode\" to decrypt, type \"decode\" to decrypt: ")
    message = input("Type your message: ").lower()                               # These 3 variables tell us what
                                                                                 # mode are we using, the message to be encrypted and the number of shifts
    shift = int(input("Type the shift number: "))                                # The number of shifts mean how many times we are movig the alphabet.

    if mode ==("encode"):
        decrypted_word= ""
        for i in message:                                                          # With this for loop we find every character of the message
            if i.isalpha():                                                        # With these if and else statement we operate only with the letters
                index = alphabet.index(i)                                          # With this function we find the index of the letter in the original alphabet
                decrypted_word = decrypted_word + alphabet[(index + shift) % 26]   # The new letter will be in that index we just find + the shift number
                                                                                   # but we use the modulus so in case the shift number is bigger than 26 or the letter is near the end of the alphabet
                                                                                   # we don't get the out of range error
            else:
                decrypted_word= decrypted_word + " "
        print(f"Your encrypted message is: {decrypted_word}")
    else:
        decrypted_word = ""                                                        # Same process but this time we substract the shift number
        for i in message:
            if i.isalpha():
                index = alphabet.index(i)
                decrypted_word = decrypted_word + alphabet[(index - shift) % 26]
            else:
                decrypted_word = decrypted_word + " "

        print(f"The original message was: {decrypted_word}")

    play_again = input("Would you like to use the program again? Type \"yes\" or \"no\": ")           # With these 3 lines we break the loop
    if play_again == "no":
        play = False