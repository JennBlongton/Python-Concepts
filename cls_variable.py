# Class variable should be same for each instances.

class Employee:

    no_emp = 0
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.no_emp += 1
        # there's no point in using self.no_emp, because that won't tell us the total no. of employees, as it will be for a particular instance.

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        # We can use self.raise_amount for a particular instance if the raise_amount needs to be changed for any particular employee. 
        # We can use Employee.raise_amount if we want all employees to have same raise.
        # self.pay = int(self.pay * Employee.raise_amount)

emp_1 = Employee("Jenn","Longton", 50000)
emp_2 = Employee("Test","User",70000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# 1.04

print(emp_1.__dict__)
# {'first': 'Jenn', 'last': 'Longton', 'pay': 50000, 'email': 'Jenn.Longton@company.com'}
print(Employee.__dict__)
# {'__module__': '__main__', 'raise_amount': 1.04, '__init__': <function Employee.__init__ at 0x000001966974D280>, 'fullname': <function Employee.fullname at 0x000001966974D310>, 'apply_raise': <function Employee.apply_raise at 0x000001966974D3A0>, '__dict__': <attribute '__dict__' of 'Employee' objects>, '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}

emp_1.raise_amount = 1.05
# for using self.raise_amount 
print(emp_1.__dict__)
# {'first': 'Jenn', 'last': 'Longton', 'pay': 50000, 'email': 'Jenn.Longton@company.com', 'raise_amount': 1.05}
print(Employee.no_emp)
# 2