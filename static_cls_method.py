# Regular methods automatically takes in the instance as the first argument
# Class methods takes class as the first argument
# Static methods don't pass anything (cls, instance), so they just behave like regular functions but has a logical connection with the class.
class Employee:

    no_emp = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amnt(cls, amount):
        cls.raise_amount = amount

    # class methods as alternative constructor/Factory Method --> YOu can use these class methods in order to provide multiple ways of creating our objects
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # Use case:- suppose we wanted a simple function that would take in a date and return whether it's a workday or not, this has a logical link to our Employee class, but has no relation to any instance or class variables.
    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True

emp_1 = Employee("Jenn","Longton", 50000)
emp_2 = Employee("Test","User",70000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# 1.04 for all

Employee.set_raise_amnt(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# 1.05 for all

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-60000'
emp_str_3 = 'Jane-Payne-80000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.fullname())
# John.Doe@company.com
# John Doe

import datetime
my_date = datetime.date(2021,8,3)
print(Employee.is_workday(my_date))
# True