import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def new_game():
    user_card = []
    dealer = []
    for _ in range(2):
        user_card.append(random.choice(cards))
    for _ in range(2):
        dealer.append(random.choice(cards))

    print(f"Your hand: {user_card}, total score: {sum(user_card)}")
    print(f"Dealer first card: {dealer[0]}")
    return (user_card,dealer)

def user_next_play(hand):
    while sum(hand) < 21:
        next_play = input("Type \"get\" to get a card or type \"pass\" to pass: ")
        if next_play == "get":
            hand.append(random.choice(cards))
            if sum(hand) < 21:
                print(f"Your hand: {hand}, total score: {sum(hand)}")
                print(f"Dealer first card: {dealer[0]}")
        else:
            break
    return hand

def dealer_next_play(hand):
    while sum(hand) < 21:
        if sum(dealer) < 17:
            dealer.append(random.choice(cards))
        else:
            dealer_next_play = random.choice(["get", "pass"])
            if dealer_next_play == "get":
                dealer.append(random.choice(cards))
            else:
                break
    return hand

game = True

while game == True:
    play = input("Do you want to play a game of Blackjac? Type \"yes\" or \"no\": ").lower()
    if play == "yes":
        user_hand,dealer = new_game()
        dealer = dealer_next_play(dealer)
        user_hand = user_next_play(user_hand)
        if sum(user_hand) == sum(dealer) and sum(user_hand) < 21:
            print("It's a draw, both of you have the same core")
    else:
        game == False


