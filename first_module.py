# print("First Module name is: {}".format(__name__))
# __main__ 
# when we run the code, it first sets some special variables and __name__ is one of them

if __name__ == '__main__':
    # we can check if this file is run directly by python or is it being imported
    print("Run directly")
else:
    print("Run from Import")
    # this will be printed when we run second_mod.py file, because we imported first_module.py there