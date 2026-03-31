"""
PYTHON HOMEWORK ASSIGNMENT
Lesson Concepts:
- Dictionaries
- Functions
- If Statements
- User Input

Overview
--------
In this assignment you will fix several Python programs.

Each problem contains code that does NOT behave the way it should.
Your task is to read the description carefully and FIX the code.

Concepts practiced:
• Accessing dictionary values
• Using dictionaries inside functions
• Using if statements with dictionary data
• Using user input with dictionaries
• Returning values from functions

Do NOT delete the comments. They explain the goal of each problem.
Only modify the code necessary to make the program work correctly.
"""


# ---------------------------------------------------------
# PROBLEM 1
#
# LESSON CONCEPT
# Accessing values from a dictionary.
#
# PROBLEM DESCRIPTION
# A dictionary named `student` stores information about a student.
# The program should print the student's major.
#
# However, the program currently tries to access a key that does not exist.
#
# YOUR TASK
# Fix the code so it correctly prints the student's major.
#
# EXPECTED OUTPUT
# Computer Science
# ---------------------------------------------------------

student = {
    "name": "Alex",
    "major": "Computer Science",
    "year": "Sophomore"
}

print(student["major"])



# ---------------------------------------------------------
# PROBLEM 2
#
# LESSON CONCEPT
# Passing dictionaries into functions.
#
# PROBLEM DESCRIPTION
# The function should print the price of an item stored
# inside a dictionary called `product`.
#
# However, the function currently references a variable
# that is not defined inside the function.
#
# YOUR TASK
# Fix the function so it uses the dictionary parameter
# that was passed into the function.
#
# EXPECTED OUTPUT
# The price is 25
# ---------------------------------------------------------

product = {
    "name": "Keyboard",
    "price": 25
}

def print_price(item):
    print("The price is", product["price"])

print_price(product)



# ---------------------------------------------------------
# PROBLEM 3
#
# LESSON CONCEPT
# Using if statements with dictionary values.
#
# PROBLEM DESCRIPTION
# The dictionary stores a user's role in a system.
#
# If the role is "admin", the program should print:
# "Full access granted"
#
# Otherwise it should print:
# "Limited access"
#
# The program currently checks the WRONG dictionary key.
#
# YOUR TASK
# Fix the if statement so it checks the correct key.
#
# EXPECTED OUTPUT
# Full access granted
# ---------------------------------------------------------

user = {
    "username": "kevin123",
    "role": "admin"
}

if user["permission"] == "admin":
    print("Full access granted")
else:
    print("Limited access")



# ---------------------------------------------------------
# PROBLEM 4
#
# LESSON CONCEPT
# Returning dictionary values from a function.
#
# PROBLEM DESCRIPTION
# The function should return the stock quantity of a product.
#
# However, the function currently returns the wrong value.
#
# YOUR TASK
# Fix the return statement so it returns the stock value.
#
# EXPECTED OUTPUT
# 150
# ---------------------------------------------------------

inventory = {
    "item": "USB Cable",
    "price": 10,
    "stock": 150
}

def get_stock(product):
    return product["price"]

print(get_stock(inventory))



# ---------------------------------------------------------
# PROBLEM 5
#
# LESSON CONCEPT
# Combining user input with dictionaries and functions.
#
# PROBLEM DESCRIPTION
# The dictionary below contains several programming languages.
# The keys represent the language name.
#
# The program asks the user to type the name of a language.
#
# If the language exists in the dictionary,
# the program should print the year it was created.
#
# If the language is NOT in the dictionary,
# the program should print:
# "Language not found."
#
# However, the current code checks incorrectly
# and will not behave as intended.
#
# YOUR TASK
# Fix the if statement so the program correctly checks
# whether the user input exists in the dictionary.
#
# EXAMPLE INPUT
# Python
#
# EXPECTED OUTPUT
# Python was created in 1991
# ---------------------------------------------------------

languages = {
    "Python": 1991,
    "Java": 1995,
    "JavaScript": 1995
}

def find_language():
    name = input("Enter a programming language: ")

    if name == languages:
        print(name, "was created in", languages[name])
    else:
        print("Language not found.")

find_language()



"""
END OF HOMEWORK

Skills practiced in this assignment:

Dictionary Skills
• Accessing dictionary keys
• Reading dictionary values
• Checking if keys exist

Function Skills
• Passing dictionaries to functions
• Returning values
• Using parameters

Logic Skills
• Writing correct if statements
• Debugging incorrect code

The goal of this homework is to help you understand how
dictionaries are used inside real Python programs.
"""