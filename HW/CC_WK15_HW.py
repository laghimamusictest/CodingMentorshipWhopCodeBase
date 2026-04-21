"""
========================================================
📘 PYTHON HOMEWORK: MODULES & IMPORTS
========================================================

🎯 OBJECTIVE:
Learn how to:
- Create your own modules
- Import functions between files
- Organize code into a simple library

--------------------------------------------------------
📁 REQUIRED FILE STRUCTURE (CREATE THIS):

project/
│── main.py
│── mylib/
    │── __init__.py
    │── math_utils.py
    │── string_utils.py

--------------------------------------------------------
🧩 TASK OVERVIEW:

1. Write functions in math_utils.py
2. Write functions in string_utils.py
3. Import and use them in main.py

--------------------------------------------------------
🔢 PART 1: math_utils.py

Create these functions:

- add(a, b)
- multiply(a, b)
- square(n)

💡 HINTS:
- Use return (not print)
- square(n) = n * n

--------------------------------------------------------
🔤 PART 2: string_utils.py

Create these functions:

- to_upper(text)
- reverse(text)
- add_exclamation(text)

💡 HINTS:
- Use .upper()
- Reverse with slicing [::-1]
- Add "!" using string concatenation

--------------------------------------------------------
📦 PART 3: __init__.py

Make it possible to do:

from mylib import add

💡 HINT:
- Use: from .file import function

--------------------------------------------------------
🚀 PART 4: main.py

- Import your functions
- Call each function
- Print results

Use these inputs:
- Numbers: 2, 3, 4
- Text: "hello"

--------------------------------------------------------
✅ EXPECTED OUTPUT (example):

Add: 5
Multiply: 6
Square: 16
Upper: HELLO
Reverse: olleh
Exclaim: hello!

--------------------------------------------------------
📌 RULES:

- Do NOT put everything in one file
- Do NOT use: from module import *
- Keep functions in correct files

--------------------------------------------------------
⭐ BONUS:

Create:
mylib/number_utils.py

Function:
- is_even(n)

Use it in main.py

--------------------------------------------------------
🧪 SELF CHECK:

- Does your structure match?
- Do imports work?
- Does main.py run without errors?

========================================================
"""

# This script is intentionally not executable as a solution.
# It only displays the assignment when run.

if __name__ == "__main__":
    print(__doc__)