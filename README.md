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