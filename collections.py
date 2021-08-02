# Collections:-
# defaultdict
# OrderedDict
# Counter
# deque
# namedtuple
# enum.Enum

# *************************************DEFAULTDICT***************************************
#  Defaultdict is a sub-class of the dict class that returns a dictionary-like object. The functionality of both dictionaries and defualtdict are almost same except for the fact that defualtdict never raises a KeyError. It provides a default value for the key that does not exists.
from collections import defaultdict

colors = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

fav_color = defaultdict(list)
for name, color in colors:
    fav_color[name].append(color)

print(fav_color)
# One other very important use case is when you are appending to nested lists inside a dictionary

# *******************************ORDEREDDICT************************************************
# OrderedDict keeps its entries sorted as they are initially inserted. Overwriting a value of an existing key doesn’t change the position of that key. However, deleting and reinserting an entry moves the key to the end of the dictionary.
from collections import OrderedDict

colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
for key, value in colours.items():
    print(key, value)

# **************************************COUNTER***********************************************
# Counter is a container. Containers are objects that hold objects. They provide a way to access the contained objects and iterate over them. Examples of built in containers are Tuple, list, and dictionary. 
from collections import Counter
  
# Create a list
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
  
# Count distinct elements and print Counter aboject
print(Counter(z))

# *************************************CHAINMAP***********************************************
# Python contains a container called “ChainMap” which encapsulates many dictionaries into one unit.

import collections
  
# initializing dictionaries
dic1 = { 'a' : 1, 'b' : 2 }
dic2 = { 'b' : 3, 'c' : 4 }
  
# initializing ChainMap
chain = collections.ChainMap(dic1, dic2)
  
# printing chainMap using maps
print ("All the ChainMap contents are : ")
print (chain.maps)
# [{'b': 2, 'a': 1}, {'c': 4, 'b': 3}]

# printing keys using keys()
print ("All keys of ChainMap are : ")
print (list(chain.keys()))
# ['b', 'c', 'a']

# printing keys using keys()
print ("All values of ChainMap are : ")
print (list(chain.values()))
# [2,4,1]

# ************************************NAMEDTUPLE*************************************************
# Like dictionaries they contain keys that are hashed to a particular value. But on contrary, it supports both access from key value and iteration, the functionality that dictionaries lack.
from collections import namedtuple 
      
# Declaring namedtuple()  
Student = namedtuple('Student',['name','age','DOB'])  
      
# Adding values  
S = Student('Nandini','19','2541997')  
      
# Access using index  
print ("The Student age using index is : ",end ="")  
print (S[1])  
# The Student age using index is : 19
      
# Access using name   
print ("The Student name using keyname is : ",end ="")  
print (S.name)
# The Student name using keyname is : Nandini

