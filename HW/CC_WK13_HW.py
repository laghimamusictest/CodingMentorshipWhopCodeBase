"""
PYTHON HOMEWORK
Topic: Lists vs Arrays

Lesson Goals
------------
This homework is designed to help you understand:

1. What Python lists are
2. What Python arrays are
3. How lists and arrays are different
4. How to access and modify elements
5. When each structure should be used

Important Concept
-----------------
Lists and arrays both store multiple values, but they behave differently.

Lists:
- Built into Python
- Can store multiple data types
- More flexible

Arrays:
- Require the array module
- Can store only ONE data type
- Often used for numeric data

Each problem below contains code that is incorrect or incomplete.
Your job is to FIX the code so the program works as described.
"""

from array import array


# ---------------------------------------------------------
# PROBLEM 1
#
# LESSON CONCEPT
# Accessing elements in a list.
#
# PROBLEM DESCRIPTION
# The list below contains several fruit names.
# The program should print the fruit "banana".
#
# However, the current index used in the print statement
# does not access the correct element.
#
# YOUR TASK
# Fix the index so the program prints "banana".
#
# EXPECTED OUTPUT
# banana
# ---------------------------------------------------------

fruits = ["apple", "banana", "orange"]

print(fruits[2])



# ---------------------------------------------------------
# PROBLEM 2
#
# LESSON CONCEPT
# Lists can store different data types.
#
# PROBLEM DESCRIPTION
# The list below contains mixed data types.
# The function should print each value in the list.
#
# However, the loop currently attempts to iterate
# over the wrong variable name.
#
# YOUR TASK
# Fix the loop so it correctly prints all items.
#
# EXPECTED OUTPUT
# Alex
# 25
# 3.5
# True
# ---------------------------------------------------------

data = ["Alex", 25, 3.5, True]
#def function_name(input, input2)
def print_list(items):
    for value in items:
        print(value)

print_list(data)



# ---------------------------------------------------------
# PROBLEM 3
#
# LESSON CONCEPT
# Adding elements to a list using append().
#
# PROBLEM DESCRIPTION
# The program should add the number 40 to the list
# using the append() method.
#
# However, the code incorrectly attempts to append
# to a variable that does not exist.
#
# YOUR TASK
# Fix the code so the number 40 is added to the list.
#
# EXPECTED OUTPUT
# [10, 20, 30, 40]
# ---------------------------------------------------------

numbers = [10, 20, 30]

number_list.append(40)

print(numbers)



# ---------------------------------------------------------
# PROBLEM 4
#
# LESSON CONCEPT
# Arrays store only one data type.
#
# PROBLEM DESCRIPTION
# The array below is meant to store integers.
#
# However, one of the values is not an integer,
# which would cause the program to fail.
#
# YOUR TASK
# Fix the array so it only contains integers.
#
# EXPECTED OUTPUT
# array('i', [1, 2, 3, 4])
# ---------------------------------------------------------

numbers = array('i', [1, 2, "three", 4])

print(numbers)



# ---------------------------------------------------------
# PROBLEM 5
#
# LESSON CONCEPT
# Accessing array elements.
#
# PROBLEM DESCRIPTION
# The array below contains several numbers.
# The program should print the number 30.
#
# However, the current index is incorrect.
#
# YOUR TASK
# Fix the index so the program prints 30.
#
# EXPECTED OUTPUT
# 30
# ---------------------------------------------------------

numbers = array('i', [10, 20, 30, 40])

print(numbers[1])



# ---------------------------------------------------------
# PROBLEM 6
#
# LESSON CONCEPT
# Comparing lists and arrays.
#
# PROBLEM DESCRIPTION
# This function should determine whether the structure
# provided is a list or an array.
#
# If it is a list:
# print "This is a Python list"
#
# If it is an array:
# print "This is a Python array"
#
# However, the function currently checks the wrong condition.
#
# YOUR TASK
# Fix the if statement so it correctly identifies the structure.
#
# EXPECTED OUTPUT
# This is a Python list
# This is a Python array
# ---------------------------------------------------------

def identify_structure(structure):

    if structure == list:
        print("This is a Python list")

    else:
        print("This is a Python array")


example_list = [1, 2, 3]
example_array = array('i', [1, 2, 3])

identify_structure(example_list)
identify_structure(example_array)



# ---------------------------------------------------------
# PROBLEM 7
#
# LESSON CONCEPT
# Understanding when lists should be used instead of arrays.
#
# PROBLEM DESCRIPTION
# The program attempts to store mixed data types
# inside an array.
#
# Arrays cannot store mixed data types.
#
# YOUR TASK
# Change the structure so the program correctly
# stores the mixed data using the appropriate structure.
#
# EXPECTED OUTPUT
# ['Alex', 30, True]
# ---------------------------------------------------------

person_data = array('i', ["Alex", 30, True])

print(person_data)



"""
END OF HOMEWORK

Concepts Practiced
------------------
Lists
• Accessing elements
• Iterating through lists
• Appending items

Arrays
• Creating arrays
• Data type restrictions
• Accessing elements

Comparison
• Lists allow mixed types
• Arrays require a single data type

The purpose of this homework is to help you understand
how lists and arrays behave differently in Python.
"""