import random

# Create a variable to track the value of the die
dice_val = 0

# Create a variable to track minimum value of the die
min_val = 1

# Create a variable to track maximum value of the die
max_val = 6

# Create a random number between min_val and max_val
dice_val = random.randint(min_val, max_val)

# Print the value of the dice roll
print(dice_val)