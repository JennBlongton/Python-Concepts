# Comprehensions are constructs that allow sequences to be built from other sequences.
# list comprehensions, dictionary comprehensions, set comprehensions, generator comprehensions

# *******************************LIST COMPREHENSIONS**************************************
# List comprehensions provide a short and concise way to create lists.
# Use Case:- when you want to supply a list to a method or function to make a new list by appending to it in each iteration of the for loop. 
squared = [x**2 for x in range(10)]
print(squared)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# ******************************DICT COMPREHENSIONS***************************************
# {v: k for k, v in some_dict.items()}
# switch keys and values of a dictionary

# ******************************SET COMPREHENSION*****************************************  {}
squared = {x**2 for x in [1, 1, 2]}
print(squared)
# {1,4}

# ******************************GENERATOR COMPREHENSION***********************************
# They are also similar to list comprehensions. The only difference is that they don’t allocate memory for the whole list but generate one item at a time, thus more memory efficient.
lst = (i for i in range(30) if i % 3 == 0)
print(lst)
for l in lst:
    print(l)