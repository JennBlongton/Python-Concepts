# generators doesn't hold the entire result in the memory, it yields one at a time. Yield returns a generator object, that we can loop on
# generator () vs list [] --> More readable, better performance
# Use Case:- Working with data streams and large files
# the state of the function is remembered. That way, when next() is called on a generator object (either explicitly or implicitly within a for loop), the previously yielded variable num is incremented, and then yielded again.
nums = (num**2 for num in range(5))
print(nums)
# <generator object <genexpr> at 0x000002874DE9CA50>
print(next(nums))
# 0
print(next(nums))
# 1
print(next(nums))
# 4
print(next(nums))
# 9

# *************************Performance***************************
import sys

lst_cnt = [i*2 for i in range(10000000)]
print(sys.getsizeof(lst_cnt))
# 81528048
gen_cnt = (i*2 for i in range(10000000))
print(sys.getsizeof(gen_cnt))
# 112

# **************************Yield*********************************
# The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left off.
def next_num():
    for i in range(10):
        yield i

for num in next_num():
    print(num)