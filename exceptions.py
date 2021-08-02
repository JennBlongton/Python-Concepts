#  The code that can cause an exception to occur is put in the try block and the handling of the exception is implemented in the except block. The code in the except block will only execute if the try block runs into an exception.
# ***************************HANDLING MULTIPLE EXCEPTIONS********************************************
# first Method
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    # puuting all exceptions which are likely to occur in a tuple
    print("An error occurred. {}".format(e.args[-1]))

# second method
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    raise e
except IOError as e:
    print("An error occurred.")
    raise e
# to handle individual exceptions in separate except blocks. We can have as many except blocks as we want.

# third method
try:
    file = open('test.txt', 'rb')
except Exception as e:
    # Some logging if you want
    raise e
# This can be helpful when you have no idea about the exceptions that may be thrown by your program. If you are just looking to catch all execptions, but don’t actually care about what they are, you can even exclude the Exception as e part.

# **********************************FINALLY CLAUSE******************************************************
# The code which is wrapped in the finally clause will run whether or not an exception occurred. It might be used to perform clean-up after a script.
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")

# *********************************TRY/ELSE CLAUSE******************************************************
# we might want some code to run if no exception occurs. This can easily be achieved by using an else clause.
try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # any code that should only run if no exception occurs in the try,
    # but for which exceptions should NOT be caught
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')
# The else clause would only run if no exception occurs and it would run before the finally clause.