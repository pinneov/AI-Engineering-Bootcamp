def print_header(header):
    print(header)
    print("-" * len(header))
    print()

def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    if second == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return first / second

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            break
        except ValueError:
            print("Please enter a valid number.")
    return number

def main():
    print_header("Python Calculator")

    while True:
        first_number = get_number("First number: ")

        allowed_operators = { "+", "-", "*", "/" }

        while True:
            operator = input("Operator (+, -, *, /): ")
            if operator in allowed_operators:
                break

        second_number = get_number("Second number: ")

        try:
            if operator == "+":
                result = add(first_number, second_number)
            elif operator == "-":
                result = subtract(first_number, second_number)
            elif operator == "*":
                result = multiply(first_number, second_number)
            else:  # operator == "/"
                result = divide(first_number, second_number)
        except ZeroDivisionError as ex:
            print(ex)
        else:
            print(f"\nResult: {result}\n")

        while True:
            again = input("Perform another calculation? (y/n): ").strip().lower()
            if again == "y" or again == "n":
                break

        if again == "n":
            break
        else:
            print()

if __name__ == "__main__":
    main()
