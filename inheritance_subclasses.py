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

# Employee class inherited and developer class will have all of it's attributes and methods of our Employee class.
class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay) OR
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())

dev_1 = Developer("Jenn","Longton", 50000, 'Python')
dev_2 = Developer("Test","User",70000, 'Java')

mgr_1 = Manager('Sue','Smith',90000, [dev_1])

print(mgr_1.email)
# Sue.Smith@company.com

# mgr_1.print_emp()
# --> Jenn Longton

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emp()
# --> Test User

print(dev_1.email)
print(dev_2.email)
# Jenn.Longton@company.com
# Test.User@company.com
print(dev_2.prog_lang)
# Java