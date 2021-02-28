card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand) <= 17:
    hand.append(card_deck.pop())
    print(sum(hand))
print(hand)

# Practice: Factorials with While Loops
# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1
# write your while loop here
while current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1
# print the factorial of number
print(product)

# Practice: Factorials with For Loops
# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# write your for loop here
for num in range(2, number + 1):
    product *= num
# print the factorial of number
print(product)

# QUIZ: Count By
start_num = 2#provide some start number
end_num = 10#provide some end number that you stop when you hit
count_by = 2#provide some number to count by

break_num = start_num
# write a while loop that uses break_num as the ongoing number to
#   check against end_num
while break_num <= end_num:
    # print(break_num)
    break_num += count_by

print(break_num)


# QUIZ: Count By Check
start_num = 1#provide some start number
end_num = 10#provide some end number that you stop when you hit
count_by = 2#provide some number to count by

# write a condition to check that end_num is larger than start_num before looping
if not end_num >= start_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."
# write a while loop that uses break_num as the ongoing number to
#   check against end_num
else:
    break_num = start_num
    while break_num < end_num:
        # print(break_num)
        break_num += count_by
    result = break_num

print(result)

# QUIZ: Nearest Square
limit = 40
num = 0

# write your while loop here
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)


# QUIZ
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
odd_count = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (odd_count < 5) and (i < len_num_list):
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        odd_count += 1
    i += 1

print ("The number of odd numbers added are: {}".format(odd_count))
print ("The sum of the odd numbers added is: {}".format(list_sum))
