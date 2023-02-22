import random
print("Welcome to the Number Guessing Game!")
print("I'm thinkingof a number between 1 and 100.")
game = True
while game == True:
    difficulty = input("Chosse a difficulty. Type \"easy\" or \"hard\": ")
    if difficulty == "easy":
        attempts = 10
        number = random.randint(1, 100)
        while attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
            if guess > number:
                print("Too high")
                attempts -= 1
            elif guess < number:
                print("Too low")
                attempts -= 1
            else:
                print("Correct")
                attempts = -1
                again = input("Do you want to play again? Types \"yes\" or \"no\". ")
                if again == "yes":
                    game = True
                else:
                    game = False

        if attempts == 0:
            print("You ran out of attempts")
    else:
        attempts = 5
        number = random.randint(1, 100)
        while attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number")
            guess = int(input("Make a guess: "))
            if guess > number:
                print("Too high")
                attempts -= 1
            elif guess < number:
                print("Too low")
                attempts -= 1
            else:
                print("Correct")
                attempts = -1
                again = input("Do you want to play again? Types \"yes\" or \"no\". ")
                if again == "yes":
                    game = True
                else:
                    game = False
        if attempts == 0:
            print("You ran out of attempts")
            again = input("Do you want to play again? Types \"yes\" or \"no\". ")
            if again == "yes":
                game = True
            else:
                game = False