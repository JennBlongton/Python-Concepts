# logging to files, setting levels and formatting. Logging is a means of tracking events that happen when some software runs. Logging is important for software developing, debugging and running. 

import logging

# Debug (10) : These are used to give Detailed information, typically of interest only when diagnosing problems.
# Info (20) : These are used to Confirm that things are working as expected
# Warning (30) : These are used an indication that something unexpected happened, or indicative of some problem in the near future
# Error (40) : This tells that due to a more serious problem, the software has not been able to perform some function
# Critical (50) : This tells serious error, indicating that the program itself may be unable to continue running

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('newfile.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
# logging.basicConfig(filename='newfile.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def add(x,y):
    return x + y

def subtract(x,y):
    return x- y

def mul(x, y):
    return x * y

def divide(x,y):
    return x/y

num_1 = 20
num_2 = 4

add_result = add(num_1, num_2)
logger.debug("ADD: {} + {} = {}".format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug("Sub: {} - {} = {}".format(num_1, num_2, sub_result))

mul_result = mul(num_1, num_2)
logger.debug("Mul: {} * {} = {}".format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug("Div: {} / {} = {}".format(num_1, num_2, div_result))
# these are creating a root 