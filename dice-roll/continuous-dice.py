import random

# Create two variables to track the value of the dice
dice_val = 0
dice2_val = 0

# Create a variable to track minimum value of the die
min_val = 1

# Create a variable to track maximum value of the die
max_val = 6

roll_again = "yes"

while roll_again == "yes": # if roll_again != "yes" go to line 31
    # Code we want to repeat:
    # Create a random number between min_val and max_val
    dice_val = random.randint(min_val, max_val)

    # Create a second random number between min_val and max_val
    dice2_val = random.randint(min_val, max_val)

    # Print the value of the second dice roll
    print(dice_val, dice2_val)

    # Print "Roll the Dices Again?" and save the input to the 
    # variable roll_again
    roll_again = input("Roll the Dices Again?")

    # Go to line 15

if roll_again == "no": # Go to line 33 if roll_again != "no" go to line 35
    print("Done")
    # Go to line 40
elif roll_again == "jacob": # If yes, go to line 36. If roll_again != "jacob", go to line 38
    print("What's  up")
    # Go to line 40
else: # Go to line 39
    print("Finished")
