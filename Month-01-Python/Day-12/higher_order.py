def add(a, b):
    return a + b


operation = add

print(operation(10, 5))



def calculate(a, b, operation: function):
    return operation(a, b)


def multiply(a, b):
    return a * b


result = calculate(10, 5, multiply)

print(result)

