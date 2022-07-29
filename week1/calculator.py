import random
# Another operation that does something silly

# Substracts one number from another

# Multiples two numbers together

# Divides one number by another 

num_val = 0

min_val = random.randint(100, 200)

max_val = random.randint(900, 1000)

# python functions signatures
# def func_name(parameters):
#   code_inside_function
#   code_inside_function
# code_outside_function

# Negates a number
def negate(number):                     # defining a function called negate that takes one parameter called number
    negated = number * -1               # creating a new variable called negated that is the value of the parameter number multiplied by -1
    print(number, "negated =", negated) # calling the function print, passing in 3 variables. The first is the variable number, the second is the value "negated =", and the third is the variable negate

# Adds two numbers together
def add(number1, number2) :
    sum = number1 + number2
    print (number1, "and", number2, "added =", sum)

def subtract(number1, number2) :
    total = number1 - number2
    print (number1, "minus", number2, "=", total)

def multiply(number1, number2) :
    product = number1 * number2
    print (number1, "multiplied by", number2, "=", product)

def divide(number1, number2) :
    quotient = number1 / number2
    int_quotient = int(quotient)
    print (number1, "divided by", number2, "=", int_quotient)

def destroy(number1) :
    num_val = random.randint(min_val, max_val)
    amount = number1 * num_val
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