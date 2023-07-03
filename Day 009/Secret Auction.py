print("Welcome to the secret auction program")

auction = {}                                  # Dictionary for the bidders and their bids
game = True                                   # Variable so the auction doesn't stop until we say so

while game == True:

    name = input("What is your name?: ")
    bid = int(input("What is your bid?: €"))          # Variables that will go into the dictionary
    auction[name] = bid                               # Addition to the dictionary

    other = input("Are there any other bidders? Types \"yes\" or \"no\": ").lower()

    if other == "no":                                 # We decide the highest bid and its bidder

        bids = []                                     # Bids list in which we will add all the bids and obtain maximum value with the max() function.
        bidder = None

        for key in auction:                           # Adding all values
            bids.append(auction[key])

        for k,v in auction.items():                   # Finding the bidder.
                                                      # .items() function is a function that converts every element of a dictionary into a tuple
            if v == max(bids):
                bidder = k
                break

        print(f"The winner is {bidder} with a bid of {max(bids)}€")
        game = False                                                      # We break the loop
    else:
        print("\n"*50)                                # This is just for "clearing" the console