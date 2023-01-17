# learnPython

https://learnpython.org/
Python 3 as a starting point for Coding 


## Indentation
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

list = []
list.append() insert to  list , append() takes exactly one argument

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
``` python
print("%s is %s years old." % (name, age))
```
>        some basic argument specifiers you should know:
>        %s - String (or any object with a string representation, like numbers)
>        %d - Integers
>        %f - Floating point numbers
>        %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
>        %x/%X - Integers in hex representation (lowercase/uppercase)
