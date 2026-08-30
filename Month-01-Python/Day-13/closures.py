def create_multiplier(multiplier):
    def multiply(value):
        return value * multiplier

    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(10))
print(triple(10))


def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter1 = create_counter()
counter2 = create_counter()

print(counter1())
print(counter1())
print(counter1())
print(counter2())