# First class function:- A programming language is said to have first-class functions if it treats functions as first class citizens.
# First Class Citizens:- /First class objects, is an entity which supports all the operations generally available to other enities. Like, passed as an argument, returned from a function, and assigned to a variable,
# First Class functions allows us to treat any functions as an object.
# Use Case:- Logging and decorators

def square(x):
    return x*x

# f = square(5)
# parenthesis mean we want to execute the function

# print(square)
# <function square at 0x0000024F02A571F0>
# print(f)
# 25

# *********************************************Assigned to a variable*********************************************
# we can remove parenthesis from square and now our variable f is equal to the function.
f = square
print(square)
# <function square at 0x000001ADBB7571F0>
print(f(5))
# 25

# *******************************************Passing function as an argument**************************************
def cube(x):
    return x*x*x

def my_map(func, arg_lst):
    result = []
    for i in arg_lst:
        result.append(func(i))
    return result

cubes = my_map(cube, [1,2,3,4,5])

print(cubes)
# [1,8,27,64,125]

# ******************************************Return a function from another function********************************
def logger(msg):
    def log_msg():
        print("Log: ", msg)
    return log_msg

log_hi = logger('Hi!')
log_hi() 
# the above will execute the log_msg() function because we added () in log_hi() which is also a function and is equal to logger() function.