import numpy

global result
result = 0

def add(x, y):
    global result

    result = float(x) + float(y)
    result = numpy.format_float_positional(result, trim='-')    # removes unnecessary trailing zeroes or decimal points from result
    return result

def subtract(x, y):
    global result

    result = float(x) - float(y)
    result = numpy.format_float_positional(result, trim='-')
    return result

def multiply(x, y):
    global result

    result = float(x) * float(y)
    result = numpy.format_float_positional(result, trim='-')
    return result

def divide(x, y):
    global result

    result = float(x) / float(y)
    result = numpy.format_float_positional(result, trim='-')
    return result

while True:
    x = float(input("Input first number: "))
    y = float(input("Input second number: "))

    print("Operations: add, subtract, multiply, or divide.")
    operation = input("Which operation would you like to choose: ")

    if operation == "add":
        result = add(x, y)
        print("The answer is: ", result, '\n')

    elif operation == "subtract":
        result = subtract(x, y)
        print("The answer is: ", result, '\n')

    elif operation == "multiply":
        result = multiply(x, y)
        print("The answer is: ", result, '\n')

    elif operation == "divide":
        result = divide(x, y)
        print("The answer is: ", result, '\n')

    else:
        print("Invalid input.", '\n')


    # cont asks user if they want to perform additional operation using result and new input number
    # if yes, user will be asked to input new number and the second while loop will begin
    # otherwise, loop will break
    while True:
        cont = input("Perform new calculation with current result? Y/N: ")

        if cont == "y" or cont == "Y":
            x = result
            result = 0
            print("First number is: ", x)
            y = float(input("Input second number: "))

            print("Operations: add, subtract, multiply, or divide.")
            operation = input("Which operation would you like to choose: ")

            if operation == "add":
                print("The answer is: ", add(x, y), '\n')

            elif operation == "subtract":
                print("The answer is: ", subtract(x, y), '\n')

            elif operation == "multiply":
                print("The answer is: ", multiply(x, y), '\n')

            elif operation == "divide":
                print("The answer is: ", divide(x, y), '\n')

            else:
                print("Invalid input.", '\n')

        else:
            break


    # Restart asks user if they want to continue use of calculator with new numbers
    restart = input("Restart calculation? Y/N: ")

    if restart == "n" or restart == "N":
        print("Goodbye.\n")
        break
