# Basic Calculator Program

# Ask the user for two numbers and an operator
num1 = float(input("Enter the first number: "))
operator = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform the operation
if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operator. Please use +, -, *, or /.")
