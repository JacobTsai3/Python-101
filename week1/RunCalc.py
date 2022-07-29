from Calc import Calc

# jacobs_calculator is a variable that has it's value a Calc object
jacobs_calculator = Calc("Jacob")

jacobs_calculator.set_min_value(250)
jacobs_calculator.set_max_value(999)

# Call the calculate function for jacobs_calculator
jacobs_calculator.calculate()

# sarahs_calculator is a variable that has it's value a Calc object
sarahs_calculator = Calc("Sarah")

sarahs_calculator.set_min_value(300)
sarahs_calculator.set_max_value(888)

# Call the calculate function for sarahs_calculator
sarahs_calculator.calculate()