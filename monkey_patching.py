# monkey patch refers to dynamic (or run-time) modifications of a class or module. In Python, we can actually change the behavior of code at run-time.
# Use Case:- For instance, consider a class that has a method get_data. This method does an external lookup (on a database or web API, for example), and various other methods in the class call it. However, in a unit test, you don't want to depend on the external data source - so you dynamically replace the get_data method with a stub that returns some fixed data.
# Because Python classes are mutable, and methods are just attributes of the class, you can do this as much as you like - and, in fact, you can even replace classes and functions in a module in exactly the same way.

import monk
def monkey_f(self):
    self.a += 1
    return self.a, self.b
    # print("Monkey_f() is being called.")

# replacing address of "func" with "monkey_f"
monk.A.func = monkey_f
obj = monk.A()

#  calling function "func" whose address got replaced with function "monkey_f()"
obj.func()
# Monkey_f() is being called.
print(obj.func())
# 3