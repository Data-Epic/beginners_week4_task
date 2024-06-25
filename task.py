# Create 10 variables with numbers(2),strings(6) and booleans(2)

# Numbers
x = 5
y = 1.5

print(type(x))
print(type(y))

# Strings
s = "Hello world"
t = "Welcome To My World"
o = "THIS IS A NEW SEASON"
r = "Play_student"
c = "Her name is Tope, she's a girl"
k = "Who is she?"

print(type(s))
print(type(t))
print(type(o))
print(type(r))
print(type(c))
print(type(k))

# Boolean
var_9 = True
var_10 = False

print(type(var_9))
print(type(var_10))

# 5 Random numbers
import random
random_numbers = [random.randint(1, 10) for _ in range(5)]
dice_roll = random.randint(1, 6)
random_integer = random.randint(1, 10)
random_float = random.random()
random_uniform = random.uniform(1.0, 10.0)

print(random_numbers, dice_roll, random_integer, random_float, random_uniform)



