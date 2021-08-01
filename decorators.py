# Decorators --> A decorator is just a function that takes another function as an argument, adds some kind of functionality and then returns another function, all of this without changing the source code of the original function that you passed in. --> Use Case (logging)
def decorator_func(original_function):
    def wrapper_func():
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_func

def display():
    print('Display function ran')

decorated_display = decorator_func(display)
decorated_display()
# Wrapper executed this before display
# Display function ran

# ************ANother way of writting*********************
def decorator_func(original_function):
    def wrapper_func(*args, **kwargs):
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_func

@decorator_func
def display():
    print('Display function ran')

def display_info(name, age):
    print("Display_info ran with arguments ({}, {})".format(name, age))

display_info('Jenn',24)
display()
# Wrapper executed this before display
# Display function ran


