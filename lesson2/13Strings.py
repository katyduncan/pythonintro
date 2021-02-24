print("hello")
print('hello')

welcome_message = "Hello, welcome to Udacity!"
print(welcome_message)

# pet_halibut = "Why should I be tarred with the epithet "loony" merely because I have a pet halibut?""
# SyntaxError: invalid syntax

pet_halibut = 'Why should I be tarred with the epithet "loony" merely because I have a pet halibut?'
salesman = '"I think you\'re an encyclopedia salesman"'
this_string = "Simon's skateboard is in the garage."
print(this_string)

# Combine strings with +
first_word = "Hello"
second_word = "There"
print(first_word + " " + second_word)
print(first_word[0])
print(first_word[1])

# Repeat strings with *
word = "Hello"
print(word * 5)

# Length function
udacity_length = len("Udacity")
print(udacity_length)

print(len("ababa") / len("ab"))


# QUIZ
# TODO: Fix this string!
# ford_quote = 'Whether you think you can, or you think you can't--you're right.'
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'


# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"
message = username + " accessed the site " + url + " at " + timestamp + "."
print(message)

# Quiz len()
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

#todo: calculate how long this name is
full_name = given_name + " " + middle_names + " " + family_name
name_length = len(full_name)
print (name_length)


# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

len(835)
