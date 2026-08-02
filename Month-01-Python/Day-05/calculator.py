def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."

    return a / b

number1 = float(input("First number: "))
number2 = float(input("Second number: "))

print(f"Addition: {add(number1, number2)}")
print(f"Subtraction: {subtract(number1, number2)}")
print(f"Multiplication: {multiply(number1, number2)}")
print(f"Division: {divide(number1, number2)}")
