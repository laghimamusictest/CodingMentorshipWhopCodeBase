"""
HOMEWORK: FIXING CONDITIONAL LOGIC IN PYTHON

Instructions for students:
- Each section below contains a broken or incomplete program
- Your task is to FIX the code so it behaves as described
- Do NOT add new concepts
- Use only: if, else, elif, numbers, strings, lists, %, indentation
- Run the program after each fix to confirm the output
"""

print("===== START OF HOMEWORK =====\n")

# --------------------------------------------------
# QUESTION 1: Fixing a Missing Condition
# Lesson goal:
# Understand that an if statement must correctly describe the decision

# PROBLEM:
# This program should print "Positive" only if the number is greater than 0.
# Right now, it prints "Positive" even when the number is negative.

x = -5

if True:
    print("Q1 Output: Positive")
else:
    print("Q1 Output: Not positive")

# TASK:
# Replace the condition so the program behaves correctly.

# EXPECTED OUTPUT AFTER FIX:
# Q1 Output: Not positive

print("\n-----------------------------\n")

# --------------------------------------------------
# QUESTION 2: Fixing an Incorrect Comparison
# Lesson goal:
# Learn how equality checks work using ==

x = 10

# PROBLEM:
# This program is supposed to print "Ten" when x equals 10,
# but it does not work correctly.

if x = 10:
    print("Q2 Output: Ten")
else:
    print("Q2 Output: Not ten")

# TASK:
# Fix the condition so the program correctly checks equality.

# EXPECTED OUTPUT AFTER FIX:
# Q2 Output: Ten

print("\n-----------------------------\n")

# --------------------------------------------------
# QUESTION 3: Fixing Even/Odd Logic
# Lesson goal:
# Use modulus (%) correctly to check even and odd numbers

x = 7

# PROBLEM:
# This program should print "Odd" for odd numbers,
# but it currently prints the wrong result.

if x % 2 == 0:
    print("Q3 Output: Odd")
else:
    print("Q3 Output: Even")

# TASK:
# Fix the logic so the output matches the number.

# EXPECTED OUTPUT AFTER FIX:
# Q3 Output: Odd

print("\n-----------------------------\n")

# --------------------------------------------------
# QUESTION 4: Fixing Indentation Errors
# Lesson goal:
# Understand how indentation controls which code belongs to if

x = 12

# PROBLEM:
# This program should only print the message if x is even AND greater than 10.
# Right now, it prints the message even when it should not.

if x % 2 == 0:
print("Q4 Output: Even and greater than 10")

# TASK:
# Fix the indentation so the logic works correctly.

# EXPECTED OUTPUT AFTER FIX:
# Q4 Output: Even and greater than 10

print("\n-----------------------------\n")

# --------------------------------------------------
# QUESTION 5: Fixing Nested Conditions
# Lesson goal:
# Learn how nested if statements control multiple decisions

x = 8

# PROBLEM:
# This program should only print the message if the number is:
# - even
# - greater than 10
# Right now, it prints the message incorrectly.

if x % 2 == 0:
    print("Q5 Output: Even and greater than 10")

# TASK:
# Add the missing condition so the program behaves correctly.

# EXPECTED OUTPUT AFTER FIX:
# (no output)

print("\n-----------------------------\n")

# --------------------------------------------------
# QUESTION 6: Fixing if / elif Order
# Lesson goal:
# Understand that Python checks conditions from top to bottom

x = 2

# PROBLEM:
# This program prints the wrong word for x = 2.

if x > 0:
    print("Q6 Output: Positive")
elif x == 2:
    print("Q6 Output: Two")

# TASK:
# Reorder or adjust conditions so the correct message prints.

# EXPECTED OUTPUT AFTER FIX:
# Q6 Output: Two

print("\n-----------------------------\n")

# --------------------------------------------------
# QUESTION 7: Fixing Missing else Case
# Lesson goal:
# Learn why else is needed to catch all remaining cases

x = 5

# PROBLEM:
# This program prints nothing for some values of x.

if x == 1:
    print("Q7 Output: One")
elif x == 2:
    print("Q7 Output: Two")

# TASK:
# Add the missing case so the program always prints something.

# EXPECTED OUTPUT AFTER FIX:
# Q7 Output: Not one or two

print("\n-----------------------------\n")

# --------------------------------------------------
# QUESTION 8: Fixing String Comparison
# Lesson goal:
# Understand how string comparisons work

animal = "cat"

# PROBLEM:
# This program should print "Cat detected" when the value is "cat",
# but it currently prints the wrong message.

if animal == "dog":
    print("Q8 Output: Cat detected")
else:
    print("Q8 Output: Dog detected")

# TASK:
# Fix the condition so the correct message prints.

# EXPECTED OUTPUT AFTER FIX:
# Q8 Output: Cat detected

print("\n-----------------------------\n")

# --------------------------------------------------
# QUESTION 9: Fixing Modulus Condition with Zero
# Lesson goal:
# Understand that zero is even

x = 0

# PROBLEM:
# This program incorrectly labels zero as odd.

if x % 2 == 1:
    print("Q9 Output: Odd")
else:
    print("Q9 Output: Even")

# TASK:
# Fix the condition so zero is handled correctly.

# EXPECTED OUTPUT AFTER FIX:
# Q9 Output: Even

print("\n-----------------------------\n")

# --------------------------------------------------
# QUESTION 10: Fixing Logic with Lists
# Lesson goal:
# Use conditions with list values

numbers = [1, 2, 3]

# PROBLEM:
# This program should print "List has three items",
# but the condition is incorrect.

if numbers == 3:
    print("Q10 Output: List has three items")
else:
    print("Q10 Output: Wrong size")

# TASK:
# Fix the condition so the program checks the list correctly.

# EXPECTED OUTPUT AFTER FIX:
# Q10 Output: List has three items

print("\n===== END OF HOMEWORK =====")
