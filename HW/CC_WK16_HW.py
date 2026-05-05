"""
========================================================
📘 PYTHON HOMEWORK: PART 3 — IMPORT SYSTEMS & DESIGN
========================================================

🎯 OBJECTIVE:
Understand how imports affect your system by:
- Creating dependencies
- Causing ripple effects
- Introducing points of failure
- Designing safer, cleaner imports

--------------------------------------------------------
📁 REQUIRED FILE STRUCTURE:

project/
│── main.py
│── mylib/
    │── __init__.py
    │── api.py
    │── math_utils.py
    │── helpers.py

--------------------------------------------------------
🧠 SYSTEM OVERVIEW (YOU ARE BUILDING THIS):

main.py → api.py → math_utils.py → helpers.py

Each layer depends on the one below it.

--------------------------------------------------------
🔧 PART 1: BUILD THE DEPENDENCY CHAIN

Create functions across files so that:

- helpers.py contains a basic function (ex: low-level logic)
- math_utils.py uses helpers.py
- api.py uses math_utils.py
- main.py ONLY imports from api.py

--------------------------------------------------------
💡 HINTS:
- Each layer should CALL the next (not duplicate logic)
- Do NOT import everything directly into main.py
- Think: “top layer should not know internal details”

--------------------------------------------------------
🧪 REQUIREMENT:

main.py must successfully call a function that depends on ALL layers.

--------------------------------------------------------
🌊 PART 2: TEST RIPPLE EFFECTS

Modify a function in helpers.py:
- Change its parameters OR return value

--------------------------------------------------------
🧪 OBSERVE:

- What breaks?
- Which files are affected?

--------------------------------------------------------
💡 QUESTIONS:
- Did the error reach main.py?
- How many files needed changes?

--------------------------------------------------------
🎯 GOAL:
Understand how one change impacts the whole system.

--------------------------------------------------------
🎯 PART 3: REDUCE COUPLING

Refactor api.py so that:

main.py only imports from api.py like this:

from mylib.api import some_function

--------------------------------------------------------
💡 HINTS:
- api.py should act as a “safe interface”
- Hide internal structure from main.py

--------------------------------------------------------
🧪 REQUIREMENT:

main.py should NOT import:
- math_utils
- helpers

--------------------------------------------------------
🔒 PART 4: CREATE A FAILURE POINT

Intentionally break something in helpers.py:
- Rename a function OR remove it

--------------------------------------------------------
🧪 OBSERVE:

- What error appears?
- Where does it show up first?

--------------------------------------------------------
💡 THINK:
- Why is this a “point of failure”?
- How many layers depended on it?

--------------------------------------------------------
⚠️ PART 5: BAD DESIGN TEST

In main.py, try importing directly:

from mylib.helpers import *

--------------------------------------------------------
🧪 OBSERVE:

- Does it work?
- Is it clean?
- Would this scale in a large project?

--------------------------------------------------------
💡 HINT:
- Think about namespace pollution
- Think about readability

--------------------------------------------------------
🚀 PART 6: IMPROVE SYSTEM DESIGN

Update __init__.py OR api.py to create a cleaner interface.

GOAL:

main.py should be simple and readable.

--------------------------------------------------------
💡 HINTS:
- Expose only what is needed
- Hide internal layers

--------------------------------------------------------
✅ EXPECTED OUTPUT (EXAMPLE):

Your output should clearly label each test:

System working: 5
After change: error observed
After refactor: system stable
Failure test: error triggered from helper layer
Bad import test: messy / unclear usage

(Exact wording may differ)

--------------------------------------------------------
📌 RULES:

- Do NOT collapse everything into one file
- Follow the file structure exactly
- Keep layers separate
- Use imports intentionally

--------------------------------------------------------
🧠 KEY CONCEPTS BEING TESTED:

- Dependency chains
- Ripple effects
- Coupling
- Abstraction layers
- Points of failure

--------------------------------------------------------
🧪 SELF CHECK:

- Does main.py only import from api.py?
- Did you observe a ripple effect?
- Can you identify the weakest point in your system?
- Did your refactor improve stability?

========================================================
"""

if __name__ == "__main__":
    print(__doc__)