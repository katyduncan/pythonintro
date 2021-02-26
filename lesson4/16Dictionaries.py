# Method 1 using for loops to create counters
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

print(word_counter)

# Method 2 using the get method
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1
print(word_counter)


# Iterating through Dicts with For Loops
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

for key in cast:
    print(key)

for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))


# QUIZ: Fruit Basket - Task 1
# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for object, count in basket_items.items():
#if the key is in the list of fruits, add the value (number of fruits) to result
    if object in fruits:
        result += count

print("There are {} fruits in the basket.".format(result))

# QUIZ: Fruit Basket - Task 2
#Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for object, count in basket_items.items():
    if object in fruits:
        result += count

print("There are {} fruits in the basket.".format(result))

#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for object, count in basket_items.items():
    if object in fruits:
        result += count

print("There are {} fruits in the basket.".format(result))


#Example 3

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for object, count in basket_items.items():
    if object in fruits:
        result += count

print("There are {} fruits in the basket.".format(result))

# QUIZ: Fruit Basket - Task 3
# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for object, count in basket_items.items():
#if the key is in the list of fruits, add to fruit_count.
    if object in fruits:
        fruit_count += count
#if the key is not in the list, then add to the not_fruit_count
    else:
        not_fruit_count += count

print("The number of fruits is {}. There are {} objects that are not fruits.".format(fruit_count, not_fruit_count))
