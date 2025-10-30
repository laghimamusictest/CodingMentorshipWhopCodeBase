"""
===========================================
PYTHON HOMEWORK — LISTS AND DEBUGGING
===========================================

This script contains 5 small problems.
Each problem has:
  - A short description
  - Buggy or incomplete code that needs fixing
  - The expected output (so you can verify your work)

Your job: fix the lines marked with  # TODO or  # BUG 
and make sure the output matches what’s expected.

-------------------------------------------
"""

# -----------------------------------------
# PROBLEM 1 — Create and Print a List
# Description:
#   The code below should print a list of 5 numbers.
#   One of the list elements is missing and print() is incorrect.
# Expected Output:
#   [10, 20, 30, 40, 50]
# -----------------------------------------

numbers = [10, 20, , 40, 50]  # BUG: missing one value
print(numbers)  # BUG: this line will not run correctly

# -----------------------------------------
# PROBLEM 2 — Accessing Elements
# Description:
#   Access the second and last element of the list.
#   The indexing is wrong.
# Expected Output:
#   Second element: 20
#   Last element: 50
# -----------------------------------------

print("Second element:", numbers[1])  # OK
print("Last element:", numbers[6])    # BUG: index out of range

# -----------------------------------------
# PROBLEM 3 — Modifying a List
# Description:
#   Insert 99 at index 2 and remove 40 from the list.
#   One method name is wrong and one argument is incorrect.
# Expected Output:
#   [10, 20, 99, 30, 50]
# -----------------------------------------

numbers.insert(2, 99)
numbers.remove(400)  # BUG: wrong value to remove
print(numbers)

# -----------------------------------------
# PROBLEM 4 — Nested Lists
# Description:
#   Combine two lists into a single list called 'combined'.
#   The syntax for combining is wrong.
# Expected Output:
#   [['apple', 'banana'], [10, 20, 30]]
# -----------------------------------------

fruits = ["apple", "banana"]
nums = [10, 20, 30]

combined = fruits + nums   # BUG: should form a list of lists, not merge elements
print(combined)

# -----------------------------------------
# PROBLEM 5 — Using List Methods
# Description:
#   Add 60 to the list, then sort it in ascending order.
#   One method call is incorrect.
# Expected Output:
#   [10, 20, 30, 50, 60, 99]
# -----------------------------------------

numbers.append(60)
numbers.sorted()  # BUG: wrong method name
print(numbers)
