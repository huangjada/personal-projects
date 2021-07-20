def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    x = float(input("Input first number: "))
    y = float(input("Input second number: "))

    print("Operations: add, subtract, multiply, or divide.")
    operation = input("Which operation would you like to choose: ")

    if operation == "add":
        print("The answer is: ", add(x, y))

    elif operation == "subtract":
        print("The answer is: ", subtract(x, y))

    elif operation == "multiply":
        print("The answer is: ", multiply(x, y))

    elif operation == "divide":
        print("The answer is: ", divide(x, y))

    else:
        print("Invalid input.")

    # cont asks user if they want to keep using calculator
    # if yes, the loop will start from the beginning again
    # otherwise, loop will break
    cont = input("Calculate new numbers? Y/N: ")

    if cont == "N" or cont == "n":
        print("Goodbye.")
        break