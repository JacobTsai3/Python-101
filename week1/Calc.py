import random

class Calc:
    # Define the state/attributes
    min_val = 0
    max_val = 0
    name = ""

    # Constructor function - Gets called whenever you create an instance of the class Calc
    def __init__(self, name):
        self.name = name

    def set_min_value(self, min_val):
        self.min_val = min_val
        print(self.name + "'s min_val = " + str(self.min_val))

    def set_max_value(self, max_val):
        self.max_val = max_val
        print(self.name + "'s max_val = " + str(self.max_val))

    # Define the functions
    def negate(self, number):                     # defining a function called negate that takes one parameter called number
        negated = number * -1               # creating a new variable called negated that is the value of the parameter number multiplied by -1
        print(number, "negated =", negated) # calling the function print, passing in 3 variables. The first is the variable number, the second is the value "negated =", and the third is the variable negate

    # Adds two numbers together
    def add(self, number1, number2) :
        sum = number1 + number2
        print (number1, "and", number2, "added =", sum)

    def subtract(self, number1, number2) :
        total = number1 - number2
        print (number1, "minus", number2, "=", total)

    def multiply(self, number1, number2) :
        product = number1 * number2
        print (number1, "multiplied by", number2, "=", product)

    def divide(self, number1, number2) :
        quotient = number1 / number2
        int_quotient = int(quotient)
        print (number1, "divided by", number2, "=", int_quotient)

    def destroy(self, number1) :
        print(self.name + "'s min_val = " + str(self.min_val))
        print(self.name + "'s max_val = " + str(self.max_val))
        num_val = 0
        num_val = random.randint(self.min_val, self.max_val)
        print(self.name + "'s num_val = " + str(num_val))
        amount = number1 * num_val
        print (number1, "destroyed =", amount)
    
    def calculate(self):
        print("Welcome to my calculator", self.name, "!")
        operation = input("Choose an operation: add, subtract, multiply, divide, negate, destroy: ")

        if operation == "negate":
            value1 = input("Give me a number to negate ")
            self.negate(int(value1))

        if operation == "add":
            number1 = input("Give me the first number to add ")
            number2 = input("Give me the second number to add ")
            self.add (int(number1), int(number2))

        if operation == "subtract":
            number1 = input("Give me a number to subtract from ")
            number2 = input("How much would you like to subtract? ")
            self.subtract (int(number1), int(number2))

        if operation == "multiply":
            number1 = input("Give me the first number to multiply ")
            number2 = input("Give me the second number to multiply ")
            self.multiply (int(number1), int(number2))

        if operation == "divide":
            number1 = input("Give me the first number to divide ")
            number2 = input("How much would you like to divide by? ")
            self.divide (int(number1), int(number2))

        if operation == "destroy":
            value1 = input("Give me a number to destroy ")
            self.destroy (int(value1))