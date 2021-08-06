# Property decorators gives us the functionality of getters, setter and deleter
class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@company.com'

    # by adding property decorator i don't have to use (), and still get the correct answer, meaning even though email is a method, but i am able to access it as an attribute.
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ") 
        self.first = first
        self.last = last   

emp_1 = Employee('Jennifer','Aniston')

emp_1.first = "Jenny"
# After changing first name, the email still remains the same (email depends on the first and last name). That will cause problem for people using our class.
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname())
# Jenny
# Jennifer.Aniston@company.com
# Jenny Aniston

# The above problem can be solved using Property decorator, which allows us to define a method, that we can access like an attribute.
# print(emp_1.email()) 
# i will have to add parenthesis, because now email is a method and anyone using our class will also have to change their code too. which we do not want.

print(emp_1.email)
# Jenny.Aniston@email.com

# ***********************************SETTTER*************************************
emp_1.fullname = "Jennifer Aniston"
# WE can't set the value of fullname like this for now, but it is possible using the setter property. (Line 18)
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
# Jennifer
# Jennifer.Aniston@email.com
# Jennifer Aniston