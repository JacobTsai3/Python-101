# nongram testing of a single line
def solve_live(number_instructions, line_of_letters) :
    # Loop through each of the number_instructions
        # Grab the number from the number_instructions array/list and call it fill_length
        # Loop through line_of_letters
            # If the letter we're on is an F
                # Start a counter for that sequence
            # If the letter we're on is an E and the counter is greater than 0
            # This means, there has been an F before this E
                # Then, compare the counter to the fill_length
                    # If the counter is not equal to the fill_length
                        # Then, this is an invalid line_of_letters, return False
                    # Otherwise (Else), reset the counter to 0, and go to the next number in the number_instructions array/list
    # If you have completed the outer loop, return True