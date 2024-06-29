first_variable = 101
second_variable = 102
third_variable = 'first string'
fourth_variable = 'second string'
fifth_variable = "third string"
sixth_variable = "fourth string"
seventh_variable = """fifth string"""
eight_variable = "sixth string"
nineth_variable = 5 > 2
tenth_variable = 2 > 5

import random
random_case_1 = (random.randrange(1, 10))
random_case_2 = (random.randrange(1, 10))
random_case_3 = (random.randrange(1, 10))
random_case_4 = (random.randrange(1, 10))
random_case_5 = (random.randrange(1, 10))

#displaying|printing
print(third_variable)
print(f'the fourth variable: {fourth_variable}')
print(seventh_variable)

print("\n")
#displaying booleans value
print(nineth_variable)
print(f'this is {tenth_variable}')

print("\n")
#using print function to display random number
print(f'displaying random numbers:')
print(random_case_1)
print(random_case_2)
print(random_case_3)

print('\n')
#some other operations
#additions of variables
added_variables = first_variable + second_variable
print(f'The addition of the first and second variable gives: {added_variables}')
#concanating strings
print('This is the ' + third_variable + ", " + fourth_variable + ", and " + fifth_variable + ".")
#addition of two random_cases
print('\n')
added_randoms = random_case_2 + random_case_4
print(f'this is the result the addition of two random_cases: {added_randoms}')