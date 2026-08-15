def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None

    return a / b

print("math_utils loaded")


# common pattern for a clear application entry point:
def main():
    print("Application started.")

if __name__ == "__main__":  # Run this block only when this file is executed directly, not when it is imported.
    main()

