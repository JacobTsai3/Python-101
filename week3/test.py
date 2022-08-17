# Typically [] "square brackets" are used when referencing arrays/lists
# and () "parenthesis" are used when making a function call, and will either be empty, (), 
# or have a list of one or more parameters (my_array) or (my_array, "hello")
# and {} "curly braces" are used to clarify function or class code - though not often used in Python.
# index == position

my_array = ['a','b','c'] # an array, also called "list", that has three items, the first 3 letters of the alphabet
print(my_array) # a function called "print", that takes in a parameter, in this case the parameter is the "my_array" array
print(my_array[0])
index = my_array.index('b')
print(index)

length = len(my_array) # length == 3
print("Length of the array:")
print(length)

range_list = range(len(my_array)) # range_list = [0,1,2]
print("Range of Length of the array:")
print(range_list) # range is first number inclusive, second number exclusive -> range(0,3) == [0,1,2]

for position in range(len(my_array)):
    print("Next index of Range of Length of the array:")
    print(position) # First time: position == 0, second time: position == 1, third time: position == 2, then the loop stops 

# print("position "+str(position)+": "+my_array[position])
# We know that position will be 0, 1, and 2 depending on which loop iteration we're on
string_position = str(0) # converts the number/integer 0 into a string
print("String version of position:")
print(string_position) # prints the string 0, not the number

value = my_array[0] # indexing into the array called "my_array" at position 0 and getting the value stored there, value == 'a'
print("Value stored at position 0 in the array:")
print(value) # prints the letter a

for position in range(len(my_array)):
    print("position "+str(position)+": "+my_array[position])

print("Array value at position 3:")
print(my_array[3])



####### Inside of Twitter's API:
class Twitter:

    def getTweet(self, tweet_id):
        tweet = someInternalFunction(tweet_id)
        data_to_return = []
        data_to_return.append(tweet.userID)
        data_to_return.append(tweet.userCreatedDate)
        data_to_return.append(tweet.tweetCreatedDate)
        return data_to_return


def printTweet:
    tweet_info = Twitter.getTweet(1228393702244134912)
    print(tweet_info)
