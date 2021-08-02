# sets behave mostly like lists with the distinction that they can not contain duplicate values. {}
# Use case:- Duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

# Methods in Sets
# Intersection()
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))
print(valid.intersection(input_set))
# red

# Difference() --> You can find the invalid values in the above example using the difference method.
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))

