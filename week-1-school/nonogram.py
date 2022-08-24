# nongram testing of a single line
# def solve_live(number_instructions, line_of_letters) :
    # Loop through each of the number_instructions
        # Grab the number from the number_instructions array/list and call it fill_length
        # Set the counter to 0
        # Loop through line_of_letters
            # If the letter we're on is an F
                # Increment the counter for that sequence
            # If the letter we're on is an E and the counter is greater than 0
            # This means, there has been an F before this E
                # Then, compare the counter to the fill_length
                    # If the counter is not equal to the fill_length
                        # Then, this is an invalid line_of_letters, return False
                    # Otherwise (Else), reset the counter to 0, and go to the next number in the number_instructions array/list
    # If you have completed the outer loop, return True

# nongram testing of a single line
    # Create an index that will track with number_instruction we're on
    # Grab the number from the number_instructions array/list and call it fill_length
    # Create a counter that will count each sequence of fills

        # If the letter we're on is an F
            # Increment the counter for that sequence
        # If the letter we're on is an E and the counter is greater than 0
        # This means, there has been an F before this E
            # Then, compare the counter to the fill_length
            # If the counter is not equal to the fill_length
                # Then, this is an invalid line_of_letters, return False
            # Otherwise (Else)
                # Reset the counter to 0
                # Increment the index
                # As long as there is another number to grab, grab it
                    # Get the length for the next sequence of fills
    # If we have gotten this far, we have a correct line of fills


# nongram testing of a single line
def solve_line(number_instructions, line_of_letters) :
    # Create an index that will track with number_instruction we're on
    index = 0
    # Grab the number from the number_instructions array/list and call it fill_length
    fill_length = number_instructions[index]
    # Create a counter that will count each sequence of fills
    counter = 0

    for letter in line_of_letters:
        # If the letter we're on is an F
        if letter == 'F':
            # Increment the counter for that sequence
            counter = counter + 1
        # If the letter we're on is an E and the counter is greater than 0
        # This means, there has been an F before this E
        elif letter == 'E' and counter > 0:
            # Then, compare the counter to the fill_length
            # If the counter is not equal to the fill_length
            if counter != fill_length:
                # Then, this is an invalid line_of_letters, return False
                return False
            # Otherwise (Else)
            else:
                # Reset the counter to 0
                counter = 0
                # Increment the index
                index = index + 1
                # As long as there is another number to grab, grab it
                if index < len(number_instructions):
                    # Get the length for the next sequence of fills
                    fill_length = number_instructions[index]
    # If we have gotten this far, we have a correct line of fills
    return True

# A set of input that should be true:
print("This should be true:")
number_instructions = [1,3,2,1]
line_of_letters = ['E','E','F','E','E','F','F','F','E','E','E','F','F','E','E','F','E']
result = solve_line(number_instructions, line_of_letters)
print(result)

# A set of input that should be false:
print("This should be false:")
number_instructions = [1,3,2,1]
line_of_letters = ['E','E','F','E','E','F','E','F','E','F','E','F','F','E','E','F','E']
result = solve_line(number_instructions, line_of_letters)
print(result)