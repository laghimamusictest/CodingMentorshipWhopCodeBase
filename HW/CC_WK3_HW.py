"""
Homework: Fix the Errors!

Goal:
-----
1. First, fix the SYNTAX ERRORS (code won’t run at all).
2. Then, fix the MATH SYNTAX ERRORS (bad math symbols, missing operators).
3. Finally, fix the LOGIC ERRORS (wrong formulas that give the wrong answers).

Tips:
- Look carefully at colons (:), parentheses (), and = signs.
- In math, remember: * means multiply, / means divide, + means add, - means subtract.
- Fix one error at a time, then run the file again.
"""

# ---------------------------
# Part 1: Syntax Errors
# ---------------------------
try:
    print("Part 1: Syntax Errors")

    # ❌ FIX ME: This has missing colons and parentheses
    x = 5
    y = 10

    if x < y
        print("x is smaller than y")

    for i in range(3)
        print("Number:", i)

    print("Part 1 finished!\n")

except Exception as e:
    print("Error in Part 1:", e)


# ---------------------------
# Part 2: Math Syntax Errors
# ---------------------------
try:
    print("Part 2: Math Syntax Errors")

    # ❌ FIX ME: These lines have math mistakes like missing * or incomplete math

    a = 10
    b = 3

    total = a +         # ❌ missing number
    product = a b       # ❌ missing * operator
    quotient = a /      # ❌ incomplete division
    result = a = b      # ❌ wrong: this assigns instead of calculating

    print("Total:", total)
    print("Product:", product)
    print("Quotient:", quotient)
    print("Result:", result)

    print("Part 2 finished!\n")

except Exception as e:
    print("Error in Part 2:", e)


# ---------------------------
# Part 3: Logic Errors
# ---------------------------
try:
    print("Part 3: Logic Errors")

    # ❌ FIX ME: These formulas are wrong but still run
    a = 10
    b = 3

    addition = a - b        # should be 13
    subtraction = a + b     # should be 7
    multiplication = a / b  # should be 30
    division = a * b        # should be about 3.33

    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Division:", division)

    print("Part 3 finished!\n")

except Exception as e:
    print("Error in Part 3:", e)


print("Homework done! Fix all 3 parts so there are no errors and the math is correct.")
