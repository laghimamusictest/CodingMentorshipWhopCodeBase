"""
Python Functions Homework
Objective: Learn how to define and use functions in Python.
Follow the instructions in the comments and test your code.
"""

# -----------------------------
# Part 1: Understanding Functions
# -----------------------------

# Task: Modify the greet function so that it prints a custom greeting.
# Change the message inside the function to say: "Welcome, [name]!"

def greet(greeting="greeting" ,name):
    # TODO: Change the line below to print "Welcome, [name]!"
    print(greeting + ", " + name + "!")

# Test Part 1
print("Part 1 Output:")
greet("Alice")  # Expected: Welcome, Alice!
greet("Bob")    # Expected: Welcome, Bob!
print()  # blank line for readability

# -----------------------------
# Part 2: Double a Number
# -----------------------------

# Task: Complete the function to return double the number given as input

def double_number(num):
    # TODO: Return num multiplied by 2
    pass

# Test Part 2
print("Part 2 Output:")
print(double_number(5))   # Expected: 10
print(double_number(10))  # Expected: 20
print()

# -----------------------------
# Part 3: Add Two Numbers
# -----------------------------

# Task: Complete the function to return the sum of two numbers

def add_numbers(a, b):
    # TODO: Return the sum of a and b
    pass

# Test Part 3
print("Part 3 Output:")
print(add_numbers(3, 4))   # Expected: 7
print(add_numbers(10, 15)) # Expected: 25
print()

# -----------------------------
# Part 4: Check if Number is Even
# -----------------------------

# Explanation:
# To check if a number is even, we can use the modulo operator (%).
# The modulo operator gives the remainder after dividing two numbers.
# Example: 
#   4 % 2 = 0  (because 4 divided by 2 leaves remainder 0)
#   7 % 2 = 1  (because 7 divided by 2 leaves remainder 1)
# Numbers with remainder 0 when divided by 2 are even; remainder 1 means odd.

# Task: Complete the function to check if a number is even or odd
# Return "Even" if the number is even, otherwise return "Odd"

def check_even(num):
    # TODO: Use the modulo operator to check if num is even or odd
    pass

# Test Part 4
print("Part 4 Output:")
print(check_even(4))  # Expected: Even
print(check_even(7))  # Expected: Odd
print()

# -----------------------------
# Part 5: Create Full Name
# -----------------------------

# Task: Complete the function to combine first_name and last_name
# Return the full name with a space in between

def full_name(first_name, last_name):
    # TODO: Return the combined full name
    pass

# Test Part 5
print("Part 5 Output:")
print(full_name("John", "Doe"))    # Expected: John Doe
print(full_name("Alice", "Smith")) # Expected: Alice Smith
print()

# -----------------------------
# Part 6: Greet Person
# -----------------------------

# Task: Complete the function to return a greeting message
# Format: "Hi, [name]! Welcome!"

def greet_person(name):
    # TODO: Return the greeting string
    pass

# Test Part 6
print("Part 6 Output:")
print(greet_person("Kevin"))  # Expected: Hi, Kevin! Welcome!
print(greet_person("Sara"))   # Expected: Hi, Sara! Welcome!
print()

# -----------------------------
# Part 7: Bonus Challenge (Optional)
# -----------------------------

# Task: Complete the function to multiply a and b, then add c
# Return the result

def multiply_and_add(a, b, c):
    # TODO: Return (a * b) + c
    pass

# Test Part 7
print("Part 7 Output:")
print(multiply_and_add(2, 3, 4))  # Expected: 10
print(multiply_and_add(5, 5, 5))  # Expected: 30