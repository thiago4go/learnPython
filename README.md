# learnPython

https://learnpython.org/
Python 3 as a starting point for Coding 

### Indentation
Python uses indentation for blocks, the standard indentation requires standard Python code to use four spaces.

## Variables and Types
Python is completely object oriented, Every variable in Python is an object.

### Variables
No need to declare type for variables, and assignaments can be done on more than one 
variable "simultaneously" on the same line.

### Numbers
1 int
1.0 float

### String
"" double quotes makes it easy to include apostrophes
''

Mixing operators between numbers and strings is not supported.
TypeError: unsupported operand type(s) for +: 'int' and 'str'

### Lists
Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Index is zero-based
```py
list = []  
list.append() #insert to  list , append() takes exactly one argument
```
### Basic Operators
#### Arithmetic Operators with numbers
number = 1 + 2 * 3 / 4.0
dividend % divisor = remainder
Using two multiplication symbols makes a power relationship. 7 ** 2=49  

#### Using Operators with Strings
Python supports concatenating strings using the addition operator
Python also supports multiplying strings to form a string with a repeating sequence

#### Using Operators with Lists
Lists can be joined with the addition operators   
lists with a repeating sequence using the multiplication operator [1,2,3] * 3

### String Formatting
The "%" operator is used to format a set of variables enclosed in a "tuple"together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d"
To use two or more argument specifiers, use a tuple (parentheses)
``` py
name = "thiago4go"
age = 33
print("%s is %s years old." % (name, age))
```
- some basic argument specifiers you should know:

     %s - String (or any object with a string representation, like numbers). 

     %d - Integers. 

     %f - Floating point numbers. 

     %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot. 

     %x/%X - Integers in hex representation (lowercase/uppercase). 

### Basic String Operations
```py
astring = "Hello World"
# Length 
len(astring)
# First occurrence of "W" at index
astring.index("W")
# Number of o's
astring.count("o")
# Slicing the string into bits
astring[3:7]
astring[3:7:2]
astring[::-1]
# Convert everything to UPPERCASE/lowercase
astring.upper()
pastring.lower()
# Check how a string starts/ends
astring.startswith("Hello")
astring.endswith("asdfasdfasdf")
# Split the string into separate strings
astring.split(" ") #inside the quotes set the spliter
```

### Conditions
Python uses boolean logic to evaluate conditions. True or False
```py
x = 2
y = [0, 1, 2]
#Boolean
x == 2 #equals, true
x =! 2 #not equals, false
x > 3 #false
x < 5 #true
x = 2 and x < 1 #false
x = 2 or x < 3 #true
x in y #true
x is x #true
x is not x #false
```
### Loops
There are two types of loops in Python, for and while.  
For loops can iterate over a sequence of numbers using the "range" and "xrange" functions.  
While loops repeat as long as a certain boolean condition is met. 
"break" and "continue" statements > break is used to exit a for loop or a while loop, > continue is used to skip the current block, and return to the "for" or "while" statement.
.
When the loop condition of "for" or "while" statement fails then code part in "else" is executed
```py
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
```
### Functions
Functions are a convenient method for separating code into useful blocks, allowing us to organise our code, make it more readable, reuse it, and save time.

Functions in python are defined using the block keyword "def", followed with the function's name as the block's name.
```py
def sum_two_numbers(a, b):
    return a + b
x = sum_two_numbers(2,3)
print(x)
```
### Classes and Objects
Objects are groups of variables and functions that work together as a single unit. Classes tell objects what variables and functions they can use. Classes are a kind of blueprint for making objects.
#### init()
The __init__() function, is a special function that is called when the class is being initiated. It's used for assigning values in a class.
```py
class NameClass:
    variable = "any"

    def function(self):
        print("This is a message inside the class.")

NewObjectX = NameClass()
NewObjectY = NameClass()
NewObjectZ = NameClass()

NewObjectY.variable = "thing"
NewObjectZ.variable = "you want"

print(NewObjectX.variable)
print(NewObjectY.variable)
print(NewObjectZ.variable)
```

### Dictionaries
A dictionary is a type of data that works like an array, but instead of indexes, it has keys and values. You can get to each value in a dictionary by using its key, which can be any type of object (a string, a number, a list, etc.) instead of its index.

```py
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
phonebook["Jane"] = 98127890 #add to dictionary["key"] = value
del phonebook["John"] #delete key and value
phonebook.pop("Jack") #delete key and value
for name, phone in phonebook.items():
    print("Phone number of %s is %d" % (name, phone))
```

### Modules and Packages
A piece of software with a specific task is known as a module in programming. For instance, when constructing a ping-pong game, one module may be in control of the game logic, while another module may be in control of drawing the game on screen. A separate file that can be edited independently makes up each module.
In Python, modules are merely Python files that have the .py extension added to the end of them. Both the file name and the name of the module are identical. A set of functions, classes, or variables may be defined and implemented inside a Python module.

Modules are imported from other modules using the import command.
```py
import module.py
module.funtionName

```
When you import a module, a new file with the extension.pyc is generated. This is a Python file that has been compiled. In order to avoid having to read and understand files every time modules are loaded, Python compiles files into Python bytecode. In the event that a.pyc file is present, it will be loaded in place of the.py file. The user will not be aware that this process is happening.

A module object can be imported to the main script, the current namespace, by using the from command.
A namespace is a system where every object is named and can be accessed in Python
```py
from module import functionName #import only the object funtionName
from module import * #importe all objects from module
functionName #now the object can be called without reffering to the module
```
#### Custom import name
You can load modules with any name you want. This is useful when conditionally importing a module so that the rest of the code can use the same name.
```py
 game.py
# import the draw module
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)
```
#### Module initialisation
When a module is loaded into a Python script for the first time, the module's code is executed once to initialise it. Local variables within the module act as "singletons," or variables that are initialised only once, if another module in your code imports the same module again, it will not be loaded again.

#### Extending module load path
In addition to the default local directory and built-in modules, there are a few ways to tell the Python interpreter where to look for modules. You can specify additional directories to look for modules using the environment variable PYTHONPATH.
You may also use the sys.path.append function. Execute it before running the import command
```py
PYTHONPATH=/path/to/module python game.py #This executes game.py, and enables the script to load modules from the directory, as well as the local directory.
sys.path.append("/path/to/module") #Now the directory has been added to the list of paths where modules are looked for.
```
#### Exploring built-in modules
Check out the full list of built-in modules in the Python standard library here:
https://docs.python.org/3/library/
Two very important functions come in handy when exploring modules in Python - the dir and help functions
```py
import urllib
dir(urllib)
help(urllib.urlopen)
```
#### Writing packages
Packages are namespaces containing multiple packages and modules. They're just directories, but with certain requirements. Each package in Python is a directory which MUST contain a special file called __init__.py. This file, which can be empty, indicates that the directory it's in is a Python package. That way it can be imported the same way as a module.

If we create a directory called foo, which marks the package name, we can then create a module inside that package called bar. Then we add the __init__.py file inside the foo directory.
To use the module bar, we can import it in two ways:
```py
import foo.bar
#or
from foo import bar
```
In the first example above, we have to use the foo prefix whenever we access the module bar. In the second example, we don't, because we've imported the module to our module's namespace.

```py
#print an alphabetically sorted list of all the functions in the re module containing the word a
import re

find_objects = []

for object in dir(re):
    if "a" in object:
        find_objects.append(object)

print(sorted(find_objects))
```

# this completed the basics of Python
### with these we will build 12 Beginner Python Projects
### from https://www.youtube.com/watch?v=8ext9G7xspg

Thank you for your attention and good luck!