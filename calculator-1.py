import numpy

global result
result = 0

# function to perform addition
def add(x, y):
    global result

    result = float(x) + float(y)
    result = numpy.format_float_positional(result, trim='-')    # removes unnecessary trailing zeroes or decimal points from result
    return result

# function to perform subtraction
def subtract(x, y):
    global result

    result = float(x) - float(y)
    result = numpy.format_float_positional(result, trim='-')
    return result

# function to perform multiplication
def multiply(x, y):
    global result

    result = float(x) * float(y)
    result = numpy.format_float_positional(result, trim='-')
    return result

# function to perform division
def divide(x, y):
    global result

    result = float(x) / float(y)
    result = numpy.format_float_positional(result, trim='-')
    return result

# function to perform the calculation of the desired operation
def calculate(operation, x, y):
    if operation == "add":
        add(x, y)
        print("The answer is: ", result)

    elif operation == "subtract":
        subtract(x, y)
        print("The answer is: ", result)

    elif operation == "multiply":
        multiply(x, y)
        print("The answer is: ", result)

    elif operation == "divide":
        divide(x, y)
        print("The answer is: ", result)

    else:
        print("Invalid input.", '\n')


while True:
    x = input("Input first number: ")
    y = input("Input second number: ")

    # checks if input contains only digits
    if x.isdigit() is False or y.isdigit() is False:
        print("Invalid input(s) detected.\nEnding Process. ")
        break

    x = float(x)
    y = float(y)

    print("Operations: add, subtract, multiply, or divide.")
    operation = input("Which operation would you like to choose: ")

    calculate(operation, x, y)


    # cont asks user if they want to perform additional operation using result and new input number
    # if yes, user will be asked to input new number and the second while loop will begin
    # otherwise, loop will break
    while True:
        cont = input("\nPerform new calculation with current result? Y/N: ")

        if cont == "y" or cont == "Y":
            x = result
            result = 0
            print("First number is: ", x)
            y = input("Input second number: ")

            if x.isdigit() is False or y.isdigit() is False:
                print("Invalid input(s) detected.\nEnding Process. ")
                break

            y = float(y)

            print("Operations: add, subtract, multiply, or divide.")
            operation = input("Which operation would you like to choose: ")

            calculate(operation, x, y)

        else:
            break


    # Restart asks user if they want to continue use of calculator with new numbers
    restart = input("Restart calculation? Y/N: ")

    if restart == "n" or restart == "N":
        print("\nGoodbye.\n")
        break
