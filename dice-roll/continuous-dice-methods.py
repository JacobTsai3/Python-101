import random

# Create two variables to track the value of the dice
dice_val = 0
dice2_val = 0

# Create a variable to track minimum value of the die
min_val = 1

# Create a variable to track maximum value of the die
max_val = 6

# Create a variable to track if the user wants to keep rolling
roll_again = "yes"

# A function that rolls the dice 
def roll_dice():
    # Create a random number between min_val and max_val
    dice_val = random.randint(min_val, max_val)

    # Create a second random number between min_val and max_val
    dice2_val = random.randint(min_val, max_val)

    # Print the value of the second dice roll
    print(dice_val, dice2_val)

# Calls roll_dice() 10 times
for x in range(0, 10):
    roll_dice()

# Calls roll_dice() 10 times
x = 0
while x < 10:
    roll_dice()
    x = x + 1

while roll_again == "yes":
    roll_dice()

    # Print "Roll the Dices Again?" and save the input to the 
    # variable roll_again
    roll_again = input("Roll the Dices Again?")

print("Done")