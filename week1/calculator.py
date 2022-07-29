# Another operation that does something silly

# Substracts one number from another

# Multiples two numbers together

# Divides one number by another 

# Negates the number
def negate(number):
    negated = number * -1
    print(number, "negated =", negated)

# Adds two numbers together
def add(number1, number2) :
    sum = number1 + number2
    print (number1, "and", number2, "added =", sum)

def subtract(number1, number2) :
    total = number1 - number2
    print (number1, "subtracted by", number2, "=", total)

def multiply(number1, number2) :
    product = number1 * number2
    print (number1, "multiplied by", number2, "=", product)

def divide(number1, number2) :
    quotient = number1 / number2
    print (number1, "divided by", number2, "=", quotient)

def destroy(number) :
    amount = print ("undefined")
    print (number1, "destroyed =", amount)

print("Welcome to my calculator!")
operation = input("Choose an operation: add, subtract, multiply, divide, negate, destroy: ")

if operation == "negate":
    value1 = input("Give me a number to negate ")
    negate(int(value1))

if operation == "add":
    number1 = input("Give me the first number to add ")
    number2 = input("Give me the second number to add ")
    add (int(number1), int(number2))


if operation == "subtract":
    number1 = input("Give me a number to subtract from ")
    number2 = input("How much would you like to subtract? ")
    subtract (int(number1), int(number2))

if operation == "multiply":
    number1 = input("Give me the first number to multiply ")
    number2 = input("Give me the second number to multiply ")
    multiply (int(number1), int(number2))

if operation == "divide":
    number1 = input("Give me the first number to divide ")
    number2 = input("How much would you like to divide by? ")
    divide (int(number1), int(number2))

if operation == "destroy":
    value1 = input("Give me a number to destroy ")
    destroy (int(value1))