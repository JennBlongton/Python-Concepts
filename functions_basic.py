# Use case:- Re-use code without repeating our code.
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Art','Psychology']
info = {'name': 'Jenn','age': 24}

student_info(*courses, **info)
# ('Art', 'Psychology')
# {'name': 'Jenn', 'age': 24}