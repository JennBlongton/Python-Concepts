# OS module allows us to interact with underlying Operating System in several ways
# To get the location of the current working directory os.getcwd() is used.
# Use case: --?

import os
cwd = os.getcwd()
print("Curren Working Directory: ",cwd)
print(os.name)

# To change the current working directory(CWD) os.chdir() method is used. This method changes the CWD to a specified path. It only takes a single argument as a new directory path.
# def current_path():
#     print("Current working directory before")
#     print(os.getcwd())
#     print("******************************")

# # Printing CWD before
# current_path()
   
# # Changing the CWD
# os.chdir('../')
   
# # Printing CWD after
# current_path()

# os.mkdir(), os.makedirs() --> for creating a directory.
# os.mkdir() method in Python is used to create a directory named path with the specified numeric mode. This method raise FileExistsError if the directory to be created already exists.

# ************************************************************************************************************************

# os.makedirs() method in Python is used to create a directory recursively. That means while making leaf directory if any intermediate-level directory is missing, os.makedirs() method will create them all.