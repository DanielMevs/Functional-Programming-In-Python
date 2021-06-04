#we can put functions in a list
#and iterate through the list 
#and at every iteration
#call the current function
#on the current input

import math

def double(x):
    return x * 2

def minus_one(x):
    return x - 1

def squared(x):
    return x * x

function_list = [
    squared,
    double,
    minus_one,
    math.sqrt,
]

my_number = 3

for func in function_list:
    my_number = func(my_number)

print(my_number)
