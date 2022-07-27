import random

age_val=0

min_val=1

max_val=100

# `name` has the value "Jacob", which is of type String
name = input("What is your name?")

# `favorite_number` has the value 13, which is of type integer, often called int
favorite_number = input("What is your favorite number?")

# A function `print` is called, with the parameter "Your name is " is passed in
print("Your name is ")

# A function `print` is called, with the parameter `name`, which has the value "Jacob" is passed in
print(name)

print("Your favorite number is")

print(favorite_number)

print("I predict your age to be")

age_val = random.randint(min_val, max_val)

print(age_val)
