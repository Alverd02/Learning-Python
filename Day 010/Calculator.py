def sum(a, b):
    x = a + b
    return x
def subs(a, b):
    x = a - b                       # Function of the operations
    return x
def prod(a, b):
    x = a * b
    return x
def div(a, b):
    x = a / b
    return x
def calculation(first_number):                # Calculation function
    options = {"+": sum, "-": subs, "*": prod, "/": div}          # Dictionary with the operations and their functions

    for k in options:
        print(k)

    operation = input("Pick an operation: ")
    next_number = float(input("What's the next number?: "))       # Varaibles of the program
    decimal = int(input("How many decimals?: "))

    result = options[operation](first_number, next_number)        # With the dictionary we use the operation variable as a key.
                                                                  # That key has a function as a value so we call it wit the parenthesis

    print(f"{first_number} {operation} {next_number} = {result}")

    return result

calc = True                                                      # Variable so we can create a while loop

while calc == True:                                              # as long as calc = True we are doing an entirely new claculation
    first_number = float(input("What's the first number?: "))
    result = calculation(first_number)
    option = input(f"Type \"ans\" to continue calculating with {result}, type \"new\" to star a new calculation or type \"break\": ") # Variable for choosing which loop we use
    if option == "ans":
        calc = False
    elif option == "new":
        continue
    else:
        break

while calc == False:                    # In this case we use the result of a previous calculation as a first number
    result = calculation(result)
    option = input(f"Type \"ans\" to continue calculating with {result}, type \"new\" to star a new calculation or type \"break\": ")
    if option == "ans":
        continue
    elif option == "new":
        calc = True
    else:
        break
