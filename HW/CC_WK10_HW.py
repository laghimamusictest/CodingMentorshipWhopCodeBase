#run continuously

operations = ["add", "subtract", "multiply", "divide", "quit"]

def usr_add(x, y):
    result = x + y
    print("\n" +str(result) + " result of function call")    

def usr_divide(x, y):
    result = x / y
    print("\n" +str(result) + " result of function call")

def usr_subtract(x, y):
    result = x - y 
    print("\n" +str(result) + " result of function call")

def usr_multiply(x, y):
    result = x * y 
    print("\n" +str(result) + " result of function call")
while True:
    print("\nAvailable Operations:")
    for op in operations:
        print("-", op)

    choice = input("\nChoose an operation\n").lower()

    if choice =="quit":
        print("Shutting down")
        break

    if choice not in operations:
        print("invalid operation. Try again.")
        continue
    # Get user numbers
    num1 = float(input("\nEnter first number: \n"))
    num2 = float(input("\nEnter second number: \n"))

    if choice == operations[0]:
        usr_add(num1, num2)

    if choice == operations[1]:
        usr_subtract(num1, num2)

    if choice == operations[2]:
        usr_multiply(num1, num2)

    if choice == operations[3]:
        usr_divide(num1, num2)


