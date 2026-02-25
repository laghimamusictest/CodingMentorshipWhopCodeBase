"""
PYTHON HOMEWORK: FOR LOOPS

Topics Covered:
- for loops
- Iterating over lists, strings, tuples
- range() function
- Reverse iteration
- Conditional statements inside loops

INSTRUCTIONS:
Each section below contains code that DOES NOT WORK CORRECTLY.
Your job is to FIX the program so it behaves exactly as described.

You may only use concepts covered in the lesson.
Do not introduce new topics.
"""

# --------------------------------------------------
# QUESTION 1: List Iteration Logic Error
# --------------------------------------------------

"""
PROBLEM:
This program should print only the numbers greater than 10
from the list below.

EXPECTED OUTPUT:
15
20
30

CURRENT ISSUE:
The condition inside the loop is incorrect.
"""

numbers = [5, 15, 8, 20, 3, 30]

for n in numbers:
    if n < 10:   # This condition is wrong
        print(n)



# --------------------------------------------------
# QUESTION 2: String Iteration with Filtering
# --------------------------------------------------

"""
PROBLEM:
This program should print only the vowels
from the string below.

Vowels are: a, e, i, o, u

EXPECTED OUTPUT:
e
a
i
o

CURRENT ISSUE:
The condition always evaluates as True.
Fix the logical condition.
"""

word = "education"

for ch in word:
    if ch == "a" or "e" or "i" or "o" or "u":
        print(ch)



# --------------------------------------------------
# QUESTION 3: range() Stop Value Error
# --------------------------------------------------

"""
PROBLEM:
This program should print numbers from 1 to 10 inclusive.

EXPECTED OUTPUT:
1 2 3 4 5 6 7 8 9 10

CURRENT ISSUE:
The stop value in range() is incorrect.
Fix it so 10 is included.
"""

for i in range(1, 10):
    print(i)



# --------------------------------------------------
# QUESTION 4: Reverse Iteration Error
# --------------------------------------------------

"""
PROBLEM:
This program should print numbers from 10 down to 1.

EXPECTED OUTPUT:
10 9 8 7 6 5 4 3 2 1

CURRENT ISSUE:
The range() parameters are incorrect for reverse iteration.
Fix start, stop, and/or step.
"""

for i in range(1, 10):
    print(i)



# --------------------------------------------------
# QUESTION 5: Step Value Mistake
# --------------------------------------------------

"""
PROBLEM:
This program should print all even numbers from 2 to 20.

EXPECTED OUTPUT:
2 4 6 8 10 12 14 16 18 20

CURRENT ISSUE:
The step value in range() is incorrect.
Fix the step size.
"""

for i in range(2, 21, 1):
    print(i)



# --------------------------------------------------
# QUESTION 6: Conditional Inside range() Loop
# --------------------------------------------------

"""
PROBLEM:
This program should print numbers from 1 to 20,
but skip numbers divisible by 3.

EXPECTED OUTPUT:
1 2 4 5 7 8 10 11 13 14 16 17 19 20

CURRENT ISSUE:
The condition is incorrect.
Fix the conditional logic.
"""

for i in range(1, 21):
    if i % 3 == 0:
        print(i)



# --------------------------------------------------
# QUESTION 7: Tuple Iteration Logic Error
# --------------------------------------------------

"""
PROBLEM:
This program should count how many numbers in the tuple
are greater than 50 and print the final count.

EXPECTED OUTPUT:
3

CURRENT ISSUE:
The counter logic is incorrect.
Fix the code so it counts properly.
"""

values = (10, 75, 23, 60, 90, 45)

count = 0

for v in values:
    if v > 50:
        count = 0   # This line is wrong

print(count)