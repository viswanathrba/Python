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
    https://www.linuxvmimages.com/images/centos-7/
    https://www.virtualbox.org/

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

Tuples
--------
A tuple is a collection of objects which ordered and immutable. Tuples are sequences, just like lists. The main difference between the tuples and the lists is that the tuples cannot be changed unlike lists. Tuples use parentheses, whereas lists use square brackets.
Ex: ("Bangalore, 'Chennai', 'Hyderabad', 34, 56, 391)

    count
    index
    
Lists
--------
list of comma-separated values (items) between square brackets, items in a list need not be of the same type.
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

Set
--------
Ex: {"Bangalore, 'Chennai', 'Hyderabad', 34, 56, 391}

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
Keys are unique within a dictionary while values may not be. The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.

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

