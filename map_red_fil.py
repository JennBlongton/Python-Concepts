# ********************************MAP*******************************
# Map applies a function to all the items in an input list
# Use case:- 
items = [1,2,3,4,5]
squared = list(map(lambda x: x**2, items))
print(squared)
# [1,4,9,16,25]

# 2nd example
def mul(x):
    return x*x

def add(x):
    return x+x

func = [mul, add]
for i in range(5):
    value = list(map(lambda x: x(i), func))
    print(value)
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]

# *********************************FILTER********************************
#  filter creates a list of elements for which a function returns true
# Use Case:- 
lst = range(-5,5)
less_than_zero = list(filter(lambda x: x<0, lst))
print(less_than_zero)
# [-5, -4, -3, -2, -1]

# *********************************REDUCE********************************
# Reduce is a really useful function for performing some computation on a list and returning the result. It applies a rolling computation to sequential pairs of values in a list.
from functools import reduce
product = reduce((lambda x,y: x*y),[1,2,3,4,5])
print(product)
# 120