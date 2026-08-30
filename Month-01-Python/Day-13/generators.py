
# yield returns an interator

def generate_numbers():
    yield 1
    yield 2
    yield 3

numbers = generate_numbers()

print(next(numbers))
print(next(numbers))
print(next(numbers))

def generate_numbers():
    print("Starting")

    yield 1

    print("After first yield")

    yield 2

    print("After second yield")

    yield 3

    print("Finished")

numbers = generate_numbers()

print("Generator created")

print(next(numbers))
print(next(numbers))
print(next(numbers))
#print(next(numbers))  # raises StopIteration

##################################################

# List uses a lot of memory
numbers = [
    number
    for number in range(1, 1_000_001)
]

# Generator uses less memory
def generate_numbers():
    for number in range(1, 1_000_001):
        yield number

##################################################

squares = [
    number * number
    for number in numbers
]

# generator expression
squares = (
    number * number
    for number in numbers
)

##################################################

list_values = [x * x for x in range(1_000_000)]       # The first immediately builds all the results.

generator_values = (x * x for x in range(1_000_000))  # The second produces them as they're consumed.

# Only interate a generator once - after that it will already have been consumed
 
###################################################

