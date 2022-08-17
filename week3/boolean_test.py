true_variable = True
false_variable = False

print("True variable =")
print(true_variable)
print("False variable =")
print(false_variable)

print("true and true =")
print(true_variable and true_variable)

print("true or true =")
print(true_variable or true_variable)

print("true and false =")
print(true_variable and false_variable) # -> True and False == False

print("true or false =")
print(true_variable or false_variable) # -> True or False == True

day = False
hungry = True

if(day == True):
    print("It's daytime!")

if(day):
    print("It's daytime!")

if(day == False):
    print("It's nighttime!")

# day is True
# not(day) -> not(True) -> False
if(not(day)): # If will only go in if it's True
    print("It's nighttime")

if(day and hungry):
    print("Eat lunch")

if(not(day) and hungry):
    print("Eat dinner")


# and
# Input 1 | operator | Input 2 | Evaluates to 
# True    | and      | True    | True
# False   | and      | True    | False
# True    | and      | False   | False
# False   | and      | False   | False

# or
# Input 1 | operator | Input 2 | Evaluates to 
# True    | or      | True    | True
# False   | or      | True    | True
# True    | or      | False   | True
# False   | or      | False   | False

# not 
# Input 1 | operator | Evalutes to
# True    | not      | False
# False   | not      | True

# nand
# Input 1 | operator | Input 2 | Evaluates to 
# True    | nand      | True    | False
# False   | nand      | True    | True
# True    | nand      | False   | True
# False   | nand      | False   | True

# nor
# Input 1 | operator | Input 2 | Evaluates to 
# True    | nor      | True    | False
# False   | nor      | True    | False
# True    | nor      | False   | False
# False   | nor      | False   | True

