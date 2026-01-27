"""
Interactive Text-Based Calculator
---------------------------------
This program allows the user to perform basic math operations.
The program keeps running until the user chooses to quit.
"""

# -----------------------------
# Calculator Functions
# -----------------------------

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


# -----------------------------
# Main Program
# -----------------------------

operations = ["add", "subtract", "multiply", "divide", "quit"]

print("Welcome to the Python Calculator")

while True:
    print("\nAvailable operations:")
    for op in operations:
        print("-", op)

    choice = input("\nChoose an operation: ").lower()

    if choice == "quit":
        print("Goodbye!")
        break

    if choice not in operations:
        print("Invalid operation. Try again.")
        continue

    # Get user numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform calculation
    if choice == "add":
        result = add(num1, num2)
    elif choice == "subtract":
        result = subtract(num1, num2)
    elif choice == "multiply":
        result = multiply(num1, num2)
    elif choice == "divide":
        result = divide(num1, num2)

    print("Result:", result)
