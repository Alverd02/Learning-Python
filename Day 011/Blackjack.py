import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def new_game():
    user_card = []
    dealer = []
    for _ in range(2):
        user_card.append(random.choice(cards))
    for _ in range(2):
        dealer.append(random.choice(cards))
    if sum(user_card) > 21 and 11 in user_card:
        index = user_card.index(11)
        hand[index] = 1
    if sum(dealer) > 21 and 11 in dealer:
        index = dealer.index(11)
        hand[index] = 1

    print(f"Your hand: {user_card}, total score: {sum(user_card)}")
    print(f"Dealer first card: {dealer[0]}")
    return (user_card,dealer)
def user_next_play(hand):
    while sum(hand) < 21:
        next_play = input("Type \"get\" to get a card or type \"pass\" to pass: ")
        if next_play == "get":
            hand.append(random.choice(cards))
            if sum(hand) > 21 and 11 in hand:
                index = hand.index(11)
                hand[index] = 1
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
            if sum(hand) > 21 and 11 in hand:
                index = hand.index(11)
                hand[index] = 1
        else:
            dealer_next_play = random.choice(["get", "pass"])
            if dealer_next_play == "get":
                dealer.append(random.choice(cards))
                if sum(hand) > 21 and 11 in hand:
                    index = hand.index(11)
                    hand[index] = 1
            else:
                break
    return hand
game = True
while game == True:
    play = input("Do you want to play a game of Blackjack? Type \"yes\" or \"no\": ").lower()
    if play == "yes":
        user_hand,dealer = new_game()
        dealer = dealer_next_play(dealer)
        user_hand = user_next_play(user_hand)
        print(f"Your hand: {user_hand}, total score: {sum(user_hand)}")
        print(f"Dealer hand: {dealer}, total score: {sum(dealer)}")
        if sum(dealer) == 21 or sum(user_hand) == 21:
            if sum(dealer) == 21:
                print("Blackjack!!!! Dealer wins")
            else:
                print("Blackjack!!!! You win")
        elif sum(user_hand) < 21 and sum(dealer) < 21:
            if sum(user_hand) == sum(dealer):
                print("It's a draw, both of you have the same core")
            elif sum(user_hand) > sum(dealer):
                print("You win!!!")
            else:
                print("You lose :(")
        elif sum(user_hand) > 21 or sum(dealer) > 21:
            if sum(user_hand) > 21 and sum(dealer) < 21:
                print("You went over 21, you lose.")
            elif sum(dealer) > 21 and sum(user_hand) < 21:
                print("The dealer went over 21, you win")
            else:
                print("Both of you went over ")
    else:
        game == False


