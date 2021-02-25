# List is python's version of array, zero-based indexing
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(months[0])
print(months[2])
print(months[-1])

list_of_random_things = [1, 3.4, 'a string', True]

# watch for indexing errors
# list_of_random_things[len(list_of_random_things)]
list_of_random_things[len(list_of_random_things)-1]
print(list_of_random_things[len(list_of_random_things)-1])

# Slicing
# upperbound is inclusive, lowerbound is exclusive
list_of_random_things = [1, 3.4, 'a string', True]
list_of_random_things[1:2]
# [3.4 notice returns a list rather vs indexing single element
q3 = months[6:9]
print(q3)
first_half = months[:6]
print(first_half)
second_half = months[6:]
print(second_half)


greeting = "Hello there"
print(len(greeting), len(months))
print(greeting[6:9], months[6:9])

# Membership Operators
# in and not in
print('her' in greeting, 'her' not in greeting)
print('Sunday' in months, 'Sunday' not in months)


# Lists are mutable (strings aren't)
months[3] = 'Friday'
print(months)

# QUIZ List indexing
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
num_days = days_in_month[month-1]

print(num_days)

# QUIZ Slicing Lists
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])


sentence1 = "I wish to register a complaint."
print(sentence1[30])


# New Section: List Methods
name = 'Jim'
student = name
name = 'Tim'

print(name)
print(student) #Jim


scores = ["B", "C", "A", "D", "B", "A"]
grades = scores
print("scores: " + str(scores))
print("grades: " + str(grades))
scores[3] = "B"
print("scores: " + str(scores))
print("grades: " + str(grades))

# useful functions: len() max() -> highest number or last alphabetically
# min() sorted()
sizes = [15, 6, 89, 34, 65, 35]
print(sorted(sizes))
print(sorted(sizes, reverse=True))

# join method list to strings
nautical_directions = "\n".join(["fore", "aft", "starboard", "port"])
print(nautical_directions)
names = ["Garcia", "O'Kelly", "Davis"]
print("-".join(names))
# don't forget the comma
names = ["Garcia" "O'Kelly" "Davis"]
print("-".join(names))

# append Method
python_varieties = ['Burmese Python', 'African Rock Python', 'Ball Python', 'Reticulated Python', 'Angolan Python']
python_varieties.append('Blood Python')
print(python_varieties)


# QUIZ
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))
# 4,2

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))
# Albert & Ben & Carol & Donna

names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))
# ["Albert", "Ben", "Carol", "Donna", "Eugenia"]
