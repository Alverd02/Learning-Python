import random

play = input("Do you want to play a game of Blackjac? Type \"yes\" or \"no\": ").lower()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
user_card = []
cpu_cards = []
while play == "yes":
    for _ in range(2):
        user_card.append(random.choice(cards))
    for _ in range(2):
        cpu_cards.append(random.choice(cards))
    print(f"Your cards are: {user_card}, current score: {sum(user_card)}")
    print(f"Computer first card: {cpu_cards[0]}")
    while sum(user_card) < 21:
        user_next_play = input("Type \"get\" to get a card or type \"pass\" to pass: ")
        if user_next_play == "get":
            user_card.append(random.choice(cards))
            print(f"Your cards are: {user_card}, current score: {sum(user_card)}")
            print(f"Computer first card: {cpu_cards[0]}")
            if sum(user_card) > 21:
                print("You went over 21")
                print('You lose :(')
                play = "no"
        else:
            break
    while sum(cpu_cards) < 21:
        cpu_next_play = random.choice(["get", "pas"])
        if cpu_next_play == "get":
            cpu_cards.append(random.choice(cards))
            if sum(cpu_cards) > 21:
                print("The computer went over 21")
                print("You win!!!")
                play = "no"
        else:
            break

