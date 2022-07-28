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

print("Welcome to my calculator!")
operation = input("Choose an operation: add, subtract, multiply, divide, negate: ")

if operation == "negate":
    value1 = input("Give me a number to negate ")
    negate(int(value1))

if operation == "add":
    number1 = input("Give me the first number to add ")
    number2 = input("Give me the second number to add ")
    add (int(number1), int(number2))