# Monkey Patching --> Replacing methods and attributes at runtime.
class A:
    a = 1
    b = 'Jenn'
    def func(self):
        # self.a +=1
        print("Func() is being called.")