# **Python Tutorial**

------------------------
# **Day 1**
------------------------


To check if Python is Installed
--------------------------------
Go To command prompt
C:\> python

To check Python version
-----------------------
C:\>python --version

Download 3.7.8 from Python.org (64bit/34bit)
select path check box without fail during installation

Notepad++ : install notepad++ and use this as editor

Important URL's
------------------------
    https://www.tutorialspoint.com/python/
    https://www.programiz.com/python-programming

Introduction
----------------  
##### Keywords 
Reserved words in Python, keywords are case sensitive.
There are 33 keywords in Python 3.7 (Ex: False, True, if , else, in, import, def, for, while, with, or, as etc..).

##### Identifiers 
Names given to variables, functions, etc. Cannot use keyword as a variable name, function name or any other identifier.

##### Statements
Instructions that a Python interpreter can execute are called statements. Ex: Assignment statement a = 1.

##### Indentation
C, C++, and Java use braces { } to define a block of code.
Python uses indentation. code block (body of a function, loop, etc.) starts with indentation and ends with the first unindented line.
Four whitespaces are used for indentation

##### Comments
use the hash(#) symbol at the beginning of each line.
Or use triple quotes, either ''' or """.


Assigning value to variables
---------------------
    a = "Hello"
    b = 1
    C = 23.6
    
    a = b = c = "Hello"
    
    a, b, c = "hello", 1, 23.6


Data Types
-----------
    Numbers
    Strings
    Tuples
    Dictionary
    Lists
    Sets

Numbers
---------
        integer  (1,10000,-34,0x431 etc..)
        float (0.0, 234.4543, -435.334 etc...)
        complex (32e+565J, -54e+45J etc..)
Strings
---------
Strings in Python are identified as a contiguous set of characters represented in the quotation marks. Python allows either pair of single or double quotes.
Subsets of strings can be taken using the slice operator [ ] & [ : ]

String Special Operators : + , *, [], [:], in, not in, %

String Methods :

    capitalize()
    center(width, fillchar)
    count(str, beg= 0,end=len(string))
    Decode
    Encode
    endswith(suffix)
    expandtabs()
    find
    index
    isalnum()
    isalpha()
    isdigit()
    isnumeric
    islower()
    len(string)
    lower()
    upper()
    etc...
    




------------------------
# **Day 2**
------------------------

Lists
--------
Most used datatype in Python, list of comma-separated values (items) between square brackets, items in a list need not be of the same type.
Lists are mutable, the value of elements of a list can be altered.
Ex: ["Bangalore, 'Chennai', 'Hyderabad', 34, 56, 391]
   
    append
    clear
    copy
    count
    extend
    index
    insert
    pop
    remove
    reverse
    sort


Tuples
--------
A tuple is a collection of objects which ordered and immutable. Tuples are sequences, just like lists.  
The main difference between the tuples and the lists is that the tuples are immutable, cannot be changed unlike lists.  
Tuples use parentheses, whereas lists use square brackets.  
Ex: ("Bangalore, 'Chennai', 'Hyderabad', 34, 56, 391)

    count
    index
    
    
Set
--------
Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }.\n
Ex: {1, 4, 9, 6, 8}

    add
    clear
    copy
    diference
    discard
    intersection
    isdisjoint
    pop
    union
    update
    etc..

Dictionary
----------
Dictionary is an unordered collection of key-value pairs. Key and value can be of any type.
Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.
{Key: Value}
Ex: {'name': 'Alan', 'Age': '40', 'place': 'PA'}

    Clear
    Fromkeys
    Copy
    Get
    items
    keys
    pop
    popitem
    setdefault
    update
    values


Python Inputs & Outputs
----------------------
print().
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False).
curly braces {} are used as placeholders. str.format().
print("my first name is {} and last name is {}".format("Viswanath", "Reddy")).


------------------------
# **Day 3**
------------------------

If Condition
------------
    if first_condition:
        print(True) #Indentation (Four Spaces)
    elif second_condition:
        print("Elif First Message")
    elif third_conditionb:
        print("Elif Second Message")
    else:
        print(False)

New Style
   
    a = 3
    b = 45
    if a > b:print(True)
    elif a == b:print("Elif First Message")
    elif a < b:print("Elif Second Message")
    else: print(False)


Loops
----------
    For Loop
    while loop
    nested loops

