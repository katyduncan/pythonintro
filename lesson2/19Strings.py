# Method specific to object/data type vs function
# methods take hidden first argument of the object being called on
# title method capitalizes first letter of each word
print("sebastian thrun".title())

full_name = "sebastian thrun"
print(full_name.islower())
# true

print("One fish, two fish, red fish, blue fish.".count('fish'))
# 4

print(full_name.count('a'))
# 2
print(full_name.find('a'))
# 3  -> python uses 0 indexing


# Format method
print("Mohammed has {} ballons".format(27))

animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))

maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics"))

# 13.37.islower()
# returns error

# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# and try them out here
my_name = "Katy"
print(my_name.endswith("y"))
print(my_name.endswith("aty"))

numb_str = "12345"
print(numb_str.isdigit())
numb_str = "123a4"
print(not numb_str.isdigit())


# Write two lines of code below, each assigning a value to a variable
shoes = "sandals"
color = "black"

# Now write a print statement using .format() to print out a sentence and the
#   values of both of the variables
print("Today I'm wearing {} that are {}.".format(shoes, color))



# SPLIT method
new_str = "The cow jumped over the moon."
new_str.split()
print(new_str.split())
# output: ['The', 'cow', 'jumped', 'over', 'the', 'moon.']
new_str.split(' ', 3)
print(new_str.split(' ', 3))
# Output is: ['The', 'cow', 'jumped', 'over the moon.']
new_str.split('.')
print(new_str.split('.'))
# Output is:['The cow jumped over the moon', '']
new_str.split(None, 3)
print(new_str.split(None, 3))
# Output is:['The', 'cow', 'jumped', 'over the moon.']


# QUIZ
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)
# 1. What is the length of the string variable verse?
# 2. What is the index of the first occurrence of the word 'and' in verse?
# 3. What is the index of the last occurrence of the word 'you' in verse?
# 4. What is the count of occurrences of the word 'you' in the verse?
# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!

verse_length = (len(verse))
first_and_index = verse.find("and")
last_you_index = verse.rfind("you")
you_count = verse.count("you")

print(verse_length)
print(first_and_index)
print(last_you_index)
print(you_count)

print("The length of the string variable 'Verse' is {}.\nThe index of the first occurrence of the word 'and' is {}.\nThe index of the last occurrence of the word 'you' is {}.\nThe count of occurences of the word 'you' is {}.".format(verse_length, first_and_index, last_you_index, you_count))
