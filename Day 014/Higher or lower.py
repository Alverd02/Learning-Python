from game_data import data
import random
def option(A):
    B = random.choice(data)
    while B == A:
        B = random.choice(data)
    print("Compare A: " + str(A["name"]) + ", a " + str(A["description"]) + " from " + str(A["country"]))
    print("Compare B: " + str(B["name"]) + ", a " + str(B["description"]) + " from " + str(B["country"]))
    return B
def compare(a):
    score = 0
    b = option(a)
    game = True
    while game == True:
        guess = input("Who has more followers? Type \"A\" or \"B\": ").upper()
        if guess == "A" and a["follower_count"] < b["follower_count"]:
            print(f"Sorry, that's wrong. Final score: {score}")
            game = False
        elif guess == "A" and a["follower_count"] > b["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}\n")
            a = b
            b = option(a)
        elif guess == "B" and a["follower_count"] > b["follower_count"]:
            print(f"Sorry, that's wrong. Final score: {score}")
            game = False
        else:
            score += 1
            print(f"You're right! Current score: {score}\n")
            a = b
            b = option(a)
def play():
    A = random.choice(data)
    compare(A)
