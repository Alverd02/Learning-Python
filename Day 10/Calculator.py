def sum(a,b):
    x = a+b
    return x
def subs(a,b):
    x = a-b
    return x
def prod(a,b):
    x = a*b
    return x
def div(a,b):
    x = a/b
    return x
def calculation(first_number):

    print("+")
    print("-")
    print("*")
    print("/")

    operation = input("Pick an operation: ")

    next_number = float(input("What's the next number?: "))
    decimal = int(input("How many decimals?: "))

    if operation == "+":
        result = round(sum(first_number, next_number), decimal)
    if operation == "-":
        result = round(subs(first_number, next_number), decimal)
    if operation == "*":
        result = round(prod(first_number, next_number), decimal)
    if operation == "/":
        result = round(div(first_number, next_number), decimal)
    return (next_number,operation,result)

calc = True

while calc == True:
    first_number = float(input("What's the first number?: "))
    next_number,operation,result = calculation(first_number)
    print(f"{first_number} {operation} {next_number} = {result}")
    option = input(f"Type \"ans\" to continue calculating with {result}, type \"new\" to star a new calculation or type \"break\": ")
    if option == "ans":
        calc = False
    elif option == "new":
        calc = True
    else:
        break
while calc == False:
    next_number,operation,result2 = calculation(result)
    print(f"{result} {operation} {next_number} = {result2}")
    option = input(f"Type \"ans\" to continue calculating with {result}, type \"new\" to star a new calculation or type \"break\": ")
    if option == "ans":
        calc = False
    elif option == "new":
        calc = True
    else:
        break