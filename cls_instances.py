# Classes allow us to logically group our data and functions in a way that's easy to re-use and also easy to build upon if need be. (data--> attributes, functions--> methods)
class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee("Jenn","Longton", 50000)
# emp_1 will be pass as self. First, last, pay and email are attributes.
emp_2 = Employee("Test","User",70000)
# these 2 are instances of class
print(emp_1)
# <__main__.Employee object at 0x0000025AFC9C78E0>
print(emp_2)
# <__main__.Employee object at 0x0000025AFCF0D1C0>

# Instance variable contains data that is unique to a particular instance
# emp_1.first = "Jenn"
# emp_1.last = "Longton"
# emp_1.email = 'jenn.Longton@company.com'
# emp_1.pay = 50000

# emp_2.first = "Test"
# emp_2.last = "User"
# emp_2.email = 'test.user@company.com'
# emp_2.pay = 70000
# Other method to create instance variable is using class as mentioned above.
print(emp_1.email)
print(emp_2.email)
# Jenn.Longton@company.com
# Test.User@company.com

print(emp_1.fullname())
# OR
print(Employee.fullname(emp_1))
# Jenn Longton

