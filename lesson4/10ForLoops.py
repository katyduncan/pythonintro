cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())
    print(city.title())

# range(start, stop, step)
print(range(4))
print(list(range(4)))

print(range(2,6))
print(list(range(2,6)))

print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(2, 10, 2)))

for number in range(4):
    print(number)


for index in range(len(cities)):
    cities[index] = cities[index].title()
    print(cities)

for i in range(3):
    print("Hello!")


# Practice: For Loops
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
# Write a for loop to print out each word in the sentence list, one word per line
for word in sentence:
    print(word)

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
for number in range(5, 31, 5):
    print(number)

# Quiz: Create Usernames
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
# write your for loop here
for name in names:
    usernames.append(name.lower().replace(" ","_"))
print(usernames)

# QUIZ: Modify Usernames with Range
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# write your for loop here
for i in range(len(usernames)):
    usernames[i] = usernames[i].lower().replace(" ","_")

print(usernames)

# QUIZ: Tag Counter
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    # if token.startswith('<') and token.endswith('>'):
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)

# QUIZ: Create an HTML List
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    # html_str += "<li>" + item + "</li>\n"
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)

# Quiz: Match Inputs to Outputs
print(list(range(0,-5))) #[]

colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = [ ]

for color in colors:
    #finish this part
    lower_colors.append(color.lower())
    lower_colors.append(lower(color))

print(lower_colors)
