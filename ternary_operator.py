#  Ternary operator --> These operators evaluate something based on a condition being true or not.
# value_if_true if condition else value_if_false
# Use Case" It allows to quickly test a condition instead of a multiline if statement
a, b = 10, 20
value = a if a<b else b
print(value)