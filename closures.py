# closures --> A closure is an inner function that remembers and has access to variables in the local scope in which it was created even after the outer fucntion has finished executing
# Use Case: Decorators concept and allows us to use first class functions concept
def outer_func():
    message = "Hi"
    def inner_func():
        print(message)
    return inner_func

my_func = outer_func
print(my_func.__name__)
# outer_func
my_func = outer_func()
print(my_func.__name__)
# inner_func
my_func()
# Hi --> Inner function executing after the outer functions has stopped execution and it still has access to message variable.