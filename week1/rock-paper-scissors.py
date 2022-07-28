import random

def rps(repeat_val):
    print("Let's play rock paper scissors", repeat_val, "times!")

    # There are three options
    # There are two players
    # Ask the user to pick rock, paper, or scissors and store their response in a variable
    user_answer = input("Pick rock, paper, or scissors ")

    # List of strings that are the choices for rock, paper, scissors
    rps_choices = ["rock", "paper", "scissors"]

    # Randomly choose rock, paper, or scissors and store that in a variable
    computer_answer = random.choice(rps_choices)
    print("The computer chose: " + computer_answer)

    # String functions that are handy:
    # name = "Sarah"
    # print(name)
    # % Sarah
    # name = name.lower()  <- convert the value to all lower case, then re-save into the same variable
    # print(name)
    # % sarah

    # if user picks rock and computer picks paper -> computer wins
    computer_wins = False
    if (((user_answer.lower() == "rock") and (computer_answer == "paper")) or
        ((user_answer.lower() == "scissors") and (computer_answer == "rock")) or
        ((user_answer.lower() == "paper") and (computer_answer == "scissors"))):
        computer_wins = True


    # if user paper and computer picks rock -> user wins
    # if user scissors and computer picks paper -> user wins
    # if user rock and computer picks scissors -> user wins
    user_wins = False
    if (((user_answer.lower() == "rock") and (computer_answer == "scissors")) or
        ((user_answer.lower() == "scissors") and (computer_answer == "paper")) or
        ((user_answer.lower() == "paper") and (computer_answer == "rock"))):
        user_wins = True

    # If user picks:
    #     rock and computer picks rock -> tie
    #     paper and computer picks paper -> tie
    #     scissors and computer picks scissors -> tie

    if user_answer.lower() == computer_answer:
        print("It was a tie!")
    elif computer_wins:
        print("computer wins")
    elif user_wins:
        print("user wins")

    # Conditionals:
    # If user picks:
    #     rock and computer picks rock -> tie
    #     paper and computer picks paper -> tie
    #     scissors and computer picks scissors -> tie

    # Conditional Statement:
    # if [condition]:
    #   [CODE]
    # elif [condition]:   <-- Optional
    #   [CODE]
    # else:               <-- Optional
    #   [CODE]

# Create a variable to track the value of my age
age_val=0

# Create a variable to track minimum value of my age
min_val=1

# Create a variable to track maximum value of my age
max_val=3

# `name` has the value "Jacob", which is of type String
name = input("What is your name? ")

# `favorite_number` has the value 13, which is of type integer, often called int
favorite_number = input("What is your favorite number? ")

# A function `print` is called, with the parameter "Your name is " is passed in
print("Your name is " + name + "and your favorite number is" + favorite_number)

# Calling the print function with comma is passing in multiple parameters
# print(string, string, variable, string)
# "stringValue stringValue variableValue stringValue"
# print("Sarah", "is so", favorite_number, "cool")
# "Sarah is so 13 cool"

# Calling the print funciton with + (concatenation) is *first* 
# concatenating the string, then passing the whole string as one parameter
# print(string + string + variable + string)
# "stringValuestringValuevariableValuestringValue"
# print("Sarah" + "is so" + name + "cool")
# "Sarahis soSarahcool"
#
# print("Sarah" + "is so" + name + "cool")
# IS EQUIVALENT TO:
# string2print = "Sarah" + "is so" + name + "cool"
# print(string2Print)

# Think PEMDAS
# x = ("Sarah" + " is cool") + (" and so is" + " Jacob")
# x = ("Sarah is cool") + (" and so is Jacob")
# x = "Sarah is cool and so is Jacob"

# A function `print` is called, with the parameter `favorite_number`, which has the value that was passed in
# print("Your favorite number is", favorite_number)

# Create a random number between min_val and max_val
age_val = random.randint(min_val, max_val)

# Print the value of my age
print("I predict your age to be", age_val)

# A for loop that uses x as an indexer and will repeat age_val number of times
for x in range(age_val) :
    rps(age_val)