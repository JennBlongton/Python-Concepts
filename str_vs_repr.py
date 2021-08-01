# the role of __repr__ is to be unambiguous
# the role of __str__ is to be readable
import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
b = str(a)

print('str(a): {}'.format(str(a)))
print('str(b): {}'.format(str(b)))
# the output is readable/userfriendly
print("**************************")
print('repr(a): {}'.format(repr(a)))
# can be used in debugging
print('repr(b): {}'.format(repr(b)))
print("**************************")