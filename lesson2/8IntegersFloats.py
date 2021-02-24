# Check data type
print(type(3))
print(type(4.3))

# whole number float
print(type(4.))

# operation involving int and float always results in float
print(3 + 2.5)

# cut decimal off float to convert to int
print(int(49.7))
# 49 no rounding occurs

# add .0 to convert int to float
print( float(3520 + 3239))
# 6759.0

# NOTE floats are approx, 0.1 is actually slightly more
print(.1 + .1 + .1 == .3)
# False
