import random

#creating variables with numbers
x = 32
y = 14

#creating variables with strings
a = "You"
b = "all"
c = "are"
d = "welcome"
e = "to"
f = "Data_Epic"
# String Concatenation with string above
g = a + " " + b + " " + c + " " + d + " " + e + " " + f

#creating variables with booleans
bool1 = (36 > 12)
bool2 = (45 > 53)

#creating the random modules to generate random numbers
random_number1 = random.randint(6, 70)
random_number2 = random.uniform(30.0, 85.5)
random_number3 = random.random()
random_number4 = random.randrange(1, 100)
random_number5 = random.choice([1, 2, 3, 4, 5, 6])


print(f"Numbers: {x}, {y}")
print(f"Strings: {g}")
print(f"Booleans: {bool1}, {bool2}")
print(f"Random Numbers: {random_number1}, {random_number2}, {random_number3}, {random_number4}, {random_number5}")
