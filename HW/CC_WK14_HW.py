# =========================================
# PYTHON IMPORTS HOMEWORK (BEGINNER)
# =========================================

# INSTRUCTIONS:
# - Fill in the missing parts (____)
# - Do NOT remove the instructions
# - Make the code run correctly
# - Match the expected output


# -----------------------------------------
# TASK 1: Importing a Module
# -----------------------------------------
# Import the "time" module
# Then use it to print the current timestamp

# WRITE YOUR CODE BELOW:
import time

print("Task 1:")
print(time.localtime())

# Expected Output:
# Task 1:
# A large number like 1712345678.123 (will be different every time)


# -----------------------------------------
# TASK 2: Importing a Specific Function
# -----------------------------------------
# Import ONLY the sleep function from time
# Then pause the program for 1 second

# WRITE YOUR CODE BELOW:
from time import sleep

print("\nTask 2:")
print("Start")
sleep(20)
print("End")

# Expected Output:
# Task 2:
# Start
# (1 second pause)
# End


# -----------------------------------------
# TASK 3: Using the random Module
# -----------------------------------------
# Import the random module
# Generate a random number between 1 and 5

# WRITE YOUR CODE BELOW:
import random

print("\nTask 3:")
num = random.randit(1, 5)
print("Number:", num)

# Expected Output:
# Task 3:
# Number: any number between 1 and 5


# -----------------------------------------
# TASK 4: Finding What’s Inside a Module
# -----------------------------------------
# Use dir() on the random module
import random
print("\nTask 4:")
print(dir(random))

# Expected Output:
# Task 4:
# A long list of names like:
# ['randint', 'choice', ...]


# -----------------------------------------
# TASK 5: Reading Documentation
# -----------------------------------------
# Use help() on the randint function from random
import random
print("\nTask 5:")
help(random)

# Expected Output:
# Task 5:
# Documentation explaining randint()


# -----------------------------------------
# TASK 6: Using the math Module
# -----------------------------------------
# Import math
# Find the square root of 25

# WRITE YOUR CODE BELOW:
import math

print("\nTask 6:")
result = math.sqrt(25)
print("Result:", result)

# Expected Output:
# Task 6:
# Result: 5.0


# =========================================
# END OF HOMEWORK
# =========================================