# Context managers allow you to allocate and release resources precisely when you want to. The most widely used example of context managers is the with statement.
# Use Case:- locking and unlocking resources and closing opened files
with open('some_file', 'w') as opened_file:
    opened_file.write('Hola!')
# The above code opens the file, writes some data to it and then closes it. If an error occurs while writing the data to the file, it tries to close it. 
file = open('some_file', 'w')
try:
    file.write('Hola!')
finally:
    file.close()
# The main advantage of using a with statement is that it makes sure our file is closed without paying attention to how the nested block exits.