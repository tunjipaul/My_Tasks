#modularizing your code 2.

#3.python modules.
#a module is a .py file that can be reused.
#importing buitl in modules (math, random, datetime)
#writing your own module (creating my_module.py and importing it)
#aliasing modules(import numbpy as np)

#a module is a file with .py extension that contains python code)functions, variables or classes) which can be reused in other programs.
#instead of writing the same code again and again, you can write it once in a module and then import it anywhere.

#importing built-in modules, python comes already with pre-built modules that you can use directly.
# #math - for mathematical operations.
# random - for generating random numbers.
# datetime - for working with dates and time. etc. to use built in modules, you have to load them into your environment, that is, "import" them.


#different ways to import modules.

#import the whole module
import math #lets put it to use.
print(math.sqrt(9)) #this imports the whole module

# # import as an alias
import math as m
# #lets put it to use
print(m.sqrt(25)) #this imports the shortened version of the math.
# #- this shortens the module name, this is common with libraries like numpy, pandas, etc.

# #3. import specific functions or variables.
from math import sqrt
print(sqrt(36)) #this is importing the fucntion - sqrt, here we don't need the prefix "math" anymore.

#4. import everything from the module.
from math import *
print(sqrt(49))
print(pi)

#writing your own module, 
# #step 1, create a folder. name it my_module
# #step 2: create a file inside the folder. name it first.py
# step 3: create another file inside the same folder. name it second.py
# step 4: create another file inside the same folder. name it main.py

#here is the folder structure.
#  refer to the folder, module.py

#4. python packages.
# a packge is a folder with init.py
#installing and using third-party packages (pip install requests, import requests)
#organizing multiple modules into a package.
#inside this folder , there must be a special file called __init__.py. this file tells python that the folder should be treated as a package.

# #- thirdparty packages.
# python comes with some built in packages but you can install extra packages created by others.
# they are stored in the python package index(pypi)
#  we install them using pip (python's package manager) or cond a

#how to install packages.

#using pip
#- this is the most common method.
#- it installs packages from pypi. it is the python's central package repository.

#to work with it, you have to use it in your terminal.
# pip install requests #install latest version
# pip install requests == 2.28 #install specific verion.
# pip install --upgrade requests #upgrade existing package.
# pip uninstall requests #remove package

# 2. using uv
