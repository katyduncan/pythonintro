# Convert float to int example
count = int(4.0)
print(count)
print(type(count))

# Convert int to string example
house_number = 13
street_name = "The Crescent"
town_name = "Belmont"
print(type(house_number))

address = str(house_number) + " " + street_name + ", " + town_name
print(address)

# Convert string to float example
grams = "35.0"
print(type(grams))
grams = float(grams)
print(type(grams))

# Gives errors
# "0" + 5
# 0 + "5"

# QUIZ
# Question 1
print(type("12"))
# str

# Question 2
print(type(12.3))
# float

# Question 3
print(type(len("my_string")))
# int

# Question 4
print(type("hippo" *12))
# str


# QUIZ - type conversion
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
total_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
print("This week's total sales: " + str(total_sales))
