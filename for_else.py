# The else clause executes after the loop completes normally. This means that the loop did not encounter a break statement.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2.0
# 5 is a prime number
# 6 equals 2 * 3.0
# 7 is a prime number
# 8 equals 2 * 4.0
# 9 equals 3 * 3.0