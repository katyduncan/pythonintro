x = 2
y = x
print(y)

# sample error
# y = z
print(y)

# efficient assignment of variables
# x = 2
# y = 3
# z = 5
x, y, z = 2, 3, 5

# better naming
x = 74728
y = 11.995
z = x/y
print(z)
# use 'snake case'
mv_population = 74728
mv_area = 11.995
mv_density = mv_population / mv_area
print(mv_density)

# assignment operators
mv_population = 74728
mv_population = 78128
print(mv_population)
mv_population = 74728
# mv_population = mv_population + 4000 - 600
mv_population += + 4000 - 600
print(mv_population)

# x = x - 2
x -= 2

#QUIZ
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
# rainfall = rainfall - (rainfall * 0.1)
# print(rainfall)
# rainfall = 5e6
# rainfall = 0.9 * rainfall
# print(rainfall)

rainfall = 5e6
rainfall *= .9
print(rainfall)


# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
print(reservoir_volume)

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
# reservoir_volume = (reservoir_volume * 1.05)
# reservoir_volume *= 1.05
reservoir_volume += reservoir_volume * 0.05
print(reservoir_volume)

# decrease reservoir_volume by 5% to account for evaporation
# reservoir_volume = reservoir_volume - (reservoir_volume * 0.05)
# reservoir_volume *= .95
reservoir_volume -= reservoir_volume * 0.05
print(reservoir_volume)

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5
print(reservoir_volume)

# print the new value of the reservoir_volume variable
print(reservoir_volume)


# QUIZ
carrots = 24
rabbits = 8
crs_per_rab = carrots/rabbits
rabbits = 12
# =3
print(crs_per_rab)
# =3