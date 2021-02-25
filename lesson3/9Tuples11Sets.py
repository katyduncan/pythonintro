location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

AngkorWat = (13.4125, 103.866667)

print(type(AngkorWat))

print("Angkor Wat is at latitude: {}".format(AngkorWat[0]))
print("Angkor Wat is at longitude: {}".format(AngkorWat[1]))

# parentheses are optional
dimensions = 52, 40, 100
length, width, height = dimensions #tuple unpacking
print("The dimensions are {}x{}x{}".format(length, width, height))


# QUIZ
tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)
print(tuple_a[1])


# Sets
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums) #{1, 2, 3, 6}

countries = ['Angola', 'Maldives', 'India', 'United States', 'India', 'Denmark', 'Sweden', 'Ghana'] #777 more countries not displayed

print(len(countries))
print(countries[:5])

country_set = set(countries)
print(len(country_set)) #196
print('India' in countries)
print('India' in country_set)

country_set.add("Italy") #as opposed to 'append' method for lists

print(country_set.pop()) #removes random element
print(country_set)
print(countries.pop()) #removes last element
print(countries)

# mathematical methods
# union, intersection, difference

# QUIZ
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()
