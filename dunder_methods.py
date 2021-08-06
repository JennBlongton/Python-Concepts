# Operator overloading --> Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example operator + is used to add two integers as well as join two strings and merge two lists. It is achievable because ‘+’ operator is overloaded by int class and str class. 

class Employee:

    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

emp_1 = Employee("Jenn","Longton", 50000)
emp_2 = Employee("Test","User",70000)

# adding 2 objects using __add__ (operator overloading example)
print(emp_1 + emp_2)
# 120000
print(repr(emp_1))
# Employee(Jenn, Longton, 50000)
print(emp_2.__str__())
# Test User - Test.User@company.com