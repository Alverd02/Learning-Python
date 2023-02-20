import random

play = input("Do you want to play a game of Blackjac? Type \"yes\" or \"no\": ").lower()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while play == "yes":
    user_card = []
    dealer = []
    for _ in range(2):
        user_card.append(random.choice(cards))
    for _ in range(2):
        dealer.append(random.choice(cards))
    print(f"Your cards are: {user_card}, current score: {sum(user_card)}")
    print(f"Computer first card: {dealer[0]}")
    while sum(user_card) < 21:
        user_next_play = input("Type \"get\" to get a card or type \"pass\" to pass: ")
        if user_next_play == "get":
            user_card.append(random.choice(cards))
            print(f"Your cards are: {user_card}, current score: {sum(user_card)}")
            print(f"Computer first card: {dealer[0]}")
        else:
            break

    while sum(dealer) < 21:
        if sum(dealer) < 17:
            dealer.append(random.choice(cards))
        else:
            dealer_next_play = random.choice(["get", "pass"])
            if dealer_next_play == "get":
                dealer.append(random.choice(cards))
            else:
                break
    print(f"Your cards are: {user_card}, current score: {sum(user_card)}")
    print(f"Your cards are: {dealer}, current score: {sum(dealer)}")
    if (sum(dealer) == sum(user_card)) and sum(dealer) <= 21:
        print("It's a draw, you have the same score.")
        play = "no"
    elif  sum(dealer) == sum(user_card) and sum(dealer) > 21:
        print("It's a draw, both user and dealer have went over 21.")
        play = "no"
    elif sum(dealer) > sum(user_card):
        print("You lose")
        play = "no"



