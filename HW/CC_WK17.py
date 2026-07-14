"""
===========================================================
        HOMEWORK: LEARNING THE VS CODE DEBUGGER
===========================================================

OBJECTIVE
---------
The purpose of this homework is NOT to practice Python syntax.
The goal is to practice using the VS Code debugger.

You should complete every problem USING THE DEBUGGER.

You should practice:

• Setting breakpoints
• Starting the debugger (F5)
• Step Over (F10)
• Step Into (F11)
• Continue (F5)
• Viewing variables
• Watching variables change
• Reading program flow
• Understanding how functions execute

-----------------------------------------------------------

INSTRUCTIONS

Each problem is commented out.

ONLY uncomment ONE problem at a time.

When you finish that problem:

1. Comment it back out.
2. Uncomment the next problem.
3. Run it in Debug Mode.
4. Complete the debugging tasks.

-----------------------------------------------------------
"""

############################################################
# PROBLEM 1
############################################################

"""
PROBLEM 1 — Watching Variables

Description
-----------
This program stores three numbers and adds them together.

Expected Input
--------------
None

Expected Output
---------------
Total: 60

Debugger Tasks
--------------
1. Place a breakpoint on the line:

       total = num1 + num2 + num3

2. Start the debugger.

3. Before executing the line, answer:

   What is num1?
   What is num2?
   What is num3?

4. Step Over (F10).

5. What is total now?

6. Continue the program.

"""

# num1 = 10
# num2 = 20
# num3 = 30
#
# total = num1 + num2 + num3
#
# print("Total:", total)


############################################################
# PROBLEM 2
############################################################

"""
PROBLEM 2 — Debugging User Input

Description
-----------
This program asks the user for two numbers.

Expected Input
--------------
First Number:
5

Second Number:
3

Expected Output
---------------
Answer: 8.0

Debugger Tasks
--------------
1. Put a breakpoint before the input() statements.

2. Continue until Python asks for input.

3. Enter:

       5
       3

4. Watch num1 and num2 appear inside the Variables panel.

5. Step Over each line.

6. Watch answer appear.

"""

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
#
# answer = num1 + num2
#
# print("Answer:", answer)


############################################################
# PROBLEM 3
############################################################

"""
PROBLEM 3 — Step Into a Function

Description
-----------
Practice using Step Into.

Expected Input
--------------
None

Expected Output
---------------
25

Debugger Tasks
--------------
1. Place a breakpoint on:

       answer = multiply(5,5)

2. Press F11 (Step Into).

3. Observe:

       a
       b

4. Step Over.

5. Observe result.

6. Continue until finished.

"""

# def multiply(a, b):
#
#     result = a * b
#
#     return result
#
#
# answer = multiply(5, 5)
#
# print(answer)


############################################################
# PROBLEM 4
############################################################

"""
PROBLEM 4 — Following Program Flow

Description
-----------
Watch how an if statement works.

Expected Input
--------------
75

Expected Output
---------------
Pass

Debugger Tasks
--------------
1. Breakpoint before the if statement.

2. Enter:

       75

3. Step Over.

4. Which branch executes?

5. Why?

"""

# grade = float(input("Enter grade: "))
#
# if grade >= 70:
#     print("Pass")
# else:
#     print("Fail")


############################################################
# PROBLEM 5
############################################################

"""
PROBLEM 5 — Watching a List Change

Description
-----------
Observe how a list changes after append().

Expected Input
--------------
None

Expected Output
---------------
['Apple', 'Banana', 'Orange']

Debugger Tasks
--------------
1. Breakpoint before append().

2. Observe the list.

3. Step Over.

4. Observe the list again.

What changed?

"""

# fruits = ["Apple", "Banana"]
#
# fruits.append("Orange")
#
# print(fruits)


############################################################
# PROBLEM 6
############################################################

"""
PROBLEM 6 — Debugging a While Loop

Description
-----------
Observe how the counter changes every iteration.

Expected Input
--------------
None

Expected Output
---------------
1
2
3
Done

Debugger Tasks
--------------
1. Breakpoint inside the loop.

2. Step through each iteration.

3. Watch count change.

4. Observe when the loop stops.

"""

# count = 1
#
# while count <= 3:
#
#     print(count)
#
#     count = count + 1
#
# print("Done")


############################################################
# PROBLEM 7
############################################################

"""
PROBLEM 7 — Debugging a Calculator Function

Description
-----------
This program adds two numbers using a function.

Expected Input
--------------
12
8

Expected Output
---------------
Result: 20.0

Debugger Tasks
--------------
1. Breakpoint on:

       result = add(num1, num2)

2. Enter:

       12
       8

3. Step Into.

4. Observe:

       a
       b

5. Execute:

       total = a + b

6. Observe total.

7. Return to the main program.

"""

# def add(a, b):
#
#     total = a + b
#
#     return total
#
#
# num1 = float(input("Enter first number: "))
#
# num2 = float(input("Enter second number: "))
#
# result = add(num1, num2)
#
# print("Result:", result)


############################################################
# PROBLEM 8
############################################################

"""
PROBLEM 8 — Finding the Bug

Description
-----------
This program is supposed to calculate the area
of a rectangle.

Expected Input
--------------
Length:
5

Width:
4

Expected Output
---------------
Area: 20

Actual Output
-------------
Area: 9

Debugger Tasks
--------------
1. DO NOT immediately fix the code.

2. Use the debugger.

3. Watch every variable.

4. Determine WHY the answer is wrong.

5. Fix the bug after finding it.

"""

# def area(length, width):
#
#     answer = length + width
#
#     return answer
#
#
# length = float(input("Length: "))
#
# width = float(input("Width: "))
#
# print("Area:", area(length, width))


############################################################
# PROBLEM 9
############################################################

"""
PROBLEM 9 — Trace Everything

Description
-----------
This problem combines variables,
functions,
if statements,
lists,
and a while loop.

Expected Input
--------------
add
5
6
quit

Expected Output
---------------
Answer: 11.0
Goodbye

Debugger Tasks
--------------
Use every debugger feature you have learned.

Watch:

• operation
• numbers
• answer
• list
• loop execution

Try to predict every variable BEFORE stepping
to the next line.

"""

# history = []
#
#
# def add(a, b):
#     return a + b
#
#
# while True:
#
#     operation = input("Operation (add/quit): ")
#
#     if operation == "quit":
#         print("Goodbye")
#         break
#
#     num1 = float(input("First Number: "))
#     num2 = float(input("Second Number: "))
#
#     answer = add(num1, num2)
#
#     history.append(answer)
#
#     print("Answer:", answer)


############################################################
# END OF HOMEWORK
############################################################

"""
Congratulations!

After completing this homework, you should be able to:

✓ Set breakpoints
✓ Start the debugger
✓ Step Over (F10)
✓ Step Into (F11)
✓ Continue (F5)
✓ Watch variables
✓ Debug functions
✓ Debug while loops
✓ Debug user input
✓ Find simple bugs using the debugger

Remember:

Professional programmers spend a significant amount of
their time debugging code.

Learning to use the debugger is one of the most valuable
skills you can develop as a programmer.
"""