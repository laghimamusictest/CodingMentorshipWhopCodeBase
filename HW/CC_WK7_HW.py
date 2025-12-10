"""
Python Homework — Function Arguments
------------------------------------

This homework practices:
- Positional arguments
- Keyword arguments
- Default arguments
- Mutability (lists changing inside functions)

For each problem:
1. Read the description
2. Follow the input/output instructions
3. Write your solution in the space provided
4. Do NOT delete the problem descriptions
"""

print("=== PYTHON HOMEWORK START ===\n")

# ---------------------------------------------------------
# PROBLEM 1 — Double a Number
# ---------------------------------------------------------
"""
Problem 1 — Double a Number
Write a function called double_number(n) that returns n * 2.

Input:
    n — an int or float
Output:
    double of n

Reason:
    Practice using a simple positional argument and returning a value.
"""

# Write your function here:
def double_number(n):
    pass


# ---------------------------------------------------------
# PROBLEM 2 — Full Name Printer
# ---------------------------------------------------------
"""
Problem 2 — Full Name Printer
Write a function print_fullname(first, last) that prints:

    First Last

Then call the function in TWO ways:
1. Positional arguments
2. Keyword arguments

Input:
    first — string
    last  — string
Output:
    Printed full name

Reason:
    Practice positional vs keyword arguments.
"""

# Write your function here:
def print_fullname(first, middle,last):
    print(first, middle, last)

# Example calls:
print_fullname("Naveen","Jean","Kumar")          # positional call
print_fullname(last="Kumar", first="Naveen", middle="Jean")      # keyword call


# ---------------------------------------------------------
# PROBLEM 3 — Greeting With a Default Value
# ---------------------------------------------------------
"""
Problem 3 — Greeting With a Default Value
Create a function:

    def greet(name="Student"):

It should print:
    Hello <name>

Call it twice:
1. With no arguments (default value used)
2. With a custom name

Input:
    name — optional string
Output:
    printed greeting

Reason:
    Practice default arguments and how they work.
"""

def greet(name="Student"):
    #code body
    return

# Example calls:
greet()           # uses default
greet("Naveen")   # custom name

#ex output
# hello Student
# hello Naveen


# ---------------------------------------------------------
# PROBLEM 4 — Modifying a List Inside a Function
# ---------------------------------------------------------
"""
Problem 4 — Modifying a List Inside a Function
Write a function add_item(lst, item) that appends item to the list lst.

Input:
    lst — a list (mutable)
    item — any value
Output:
    No return value (but lst should change!)

Reason:
    Understand how mutable objects (lists) change inside functions.
"""

def add_item(lst, item):
    lst.append(item)

# Example test:
my_list = [1, 2]
add_item(my_list, 3)
print("After add_item:", my_list)   # should be [1, 2, 3]


# ---------------------------------------------------------
# PROBLEM 5 — Total Price Calculator
# ---------------------------------------------------------
"""
Problem 5 — Total Price Calculator
Write a function total_price(price, quantity=1) that returns:

    price * quantity

Input:
    price — number
    quantity — optional number (defaults to 1)
Output:
    total cost (number)

Reason:
    Practice combining positional and default arguments.
"""

def total_price(price, quantity=1):
    pass

# Example tests:
print("Total:", total_price(5, 3))  # 15
print("Total:", total_price(10))    # 10 (default quantity)


# ---------------------------------------------------------
# PROBLEM 6 — Add Two Numbers (Error Exploration)
# ---------------------------------------------------------
"""
Problem 6 — Add Two Numbers (Error Exploration)

Write a function:
    def add(a, b):

Then call it incorrectly on purpose:
1. Missing arguments
2. Too many arguments
3. Wrong types (e.g., add("hello", 5))

Write comments explaining:
- What error happens
- Why the error happens

Reason:
    Learn to read and understand Python error messages.
"""

def add(a, b):
    return a + b

# Uncomment each line ONE AT A TIME to see the errors:

# add(5)               # ERROR: missing one argument
# add(1, 2, 3)         # ERROR: too many arguments
# add("hello", 5)      # ERROR: cannot add string + int


# ---------------------------------------------------------
# OPTIONAL CHALLENGE
# ---------------------------------------------------------
"""
OPTIONAL CHALLENGE — Repeat a Word

Write:
    def repeat(word, times=2):

Return the word repeated 'times' times.

Reason:
    Practice default arguments + string multiplication.
"""

def repeat(word, times=2):
    return word * times

print(repeat("hi"))
print(repeat("hi", 4))


print("\n=== PYTHON HOMEWORK END ===")
