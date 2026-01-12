"""
PYTHON HOMEWORK ASSIGNMENT
Topic Focus:
- Functions
- if / elif / else conditional statements
- User input
- Type conversion
- Mutable vs immutable behavior

INSTRUCTIONS:
Each program below is INCORRECT.
Read the comments carefully and FIX the code so it behaves as described.
Do NOT remove functions or conditionals.
Do NOT introduce concepts that were not taught.
"""

# --------------------------------------------------
# QUESTION 1: Function + Conditional Logic (Fix the Bug)
# --------------------------------------------------

"""
PROBLEM DESCRIPTION:
This function is supposed to determine whether a number is
positive, negative, or zero.

CURRENT ISSUE:
The function logic is incomplete and produces incorrect results.

WHAT YOU MUST FIX:
- Correct the conditional logic inside the function
- Ensure all three cases are handled

EXPECTED BEHAVIOR:
Input: 5    -> Output: Positive
Input: -2   -> Output: Negative
Input: 0    -> Output: Zero
"""

def check_number(num):
    if num >= 0:
        print("Positive")
    else:
        print("Negative")

x = int(input("Enter a number: "))
check_number(x)


# --------------------------------------------------
# QUESTION 2: Function with Input Conversion
# --------------------------------------------------

"""
PROBLEM DESCRIPTION:
This function should take two numbers and print which one is larger.

CURRENT ISSUE:
The program runs, but the comparison is incorrect.

WHAT YOU MUST FIX:
- Ensure the function receives the correct data type
- Fix the logic so the comparison works correctly

EXPECTED BEHAVIOR:
Input: 3 and 10 -> Output: Second number is larger
Input: 7 and 2  -> Output: First number is larger
"""

def compare_numbers(a, b):
    if a > b:
        print("First number is larger")
    else:
        print("Second number is larger")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

compare_numbers(num1, num2)


# --------------------------------------------------
# QUESTION 3: Even or Odd Using a Function
# --------------------------------------------------

"""
PROBLEM DESCRIPTION:
This function checks whether a number is even or odd.

CURRENT ISSUE:
The function is written correctly, but it is not used properly.

WHAT YOU MUST FIX:
- Ensure the function is called correctly
- Ensure the argument passed allows the function to work

EXPECTED BEHAVIOR:
Input: 4 -> Output: Even
Input: 9 -> Output: Odd
"""

def even_or_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

value = input("Enter a number: ")
even_or_odd   # Function is never executed


# --------------------------------------------------
# QUESTION 4: Conditional Logic Inside a Function (Lists)
# --------------------------------------------------

"""
PROBLEM DESCRIPTION:
This function should modify a list based on a condition.

RULE:
If the first number in the list is greater than 5,
change the second element to 99.

CURRENT ISSUE:
The function does not correctly modify the original list.

WHAT YOU MUST FIX:
- Fix the function so the original list is updated
- Do NOT create a new list

EXPECTED BEHAVIOR:
Input list: [6, 2, 3]
Output list: [6, 99, 3]

Input list: [3, 2, 3]
Output list: [3, 2, 3]
"""

def modify_list(lst):
    if lst[0] > 5:
        lst = [lst[0], 99, lst[2]]  # This breaks the lesson concept

numbers = [6, 2, 3]
modify_list(numbers)
print(numbers)


# --------------------------------------------------
# QUESTION 5: Function with Multiple Conditions (elif)
# --------------------------------------------------

"""
PROBLEM DESCRIPTION:
This function prints a message based on a user's score.

RULES:
- 90 or above  -> "Excellent"
- 70 to 89     -> "Good"
- Below 70     -> "Needs Improvement"

CURRENT ISSUE:
The conditional structure is incorrect.

WHAT YOU MUST FIX:
- Use if / elif / else correctly
- Ensure only ONE message prints

EXPECTED BEHAVIOR:
Input: 95 -> Excellent
Input: 80 -> Good
Input: 60 -> Needs Improvement
"""

def grade(score):
    if score >= 90:
        print("Excellent")
    if score >= 70:
        print("Good")
    else:
        print("Needs Improvement")

marks = int(input("Enter score: "))
grade(marks)


# --------------------------------------------------
# QUESTION 6: Function + User Choice (Characters)
# --------------------------------------------------

"""
PROBLEM DESCRIPTION:
This function checks whether a character is a vowel or consonant.

RULES:
Vowels: a, e, i, o, u

CURRENT ISSUE:
The function logic does not correctly identify vowels.

WHAT YOU MUST FIX:
- Fix the condition so vowel detection works correctly
- Only check the first character entered

EXPECTED BEHAVIOR:
Input: a -> Vowel
Input: b -> Consonant
"""

def check_letter(ch):
    if ch == 'a' or 'e' or 'i' or 'o' or 'u':
        print("Vowel")
    else:
        print("Consonant")

letter = input("Enter a letter: ")
check_letter(letter)
