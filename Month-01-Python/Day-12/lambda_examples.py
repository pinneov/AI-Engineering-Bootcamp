
# def square(number):
#     return number * number

# lambda parameters: expression

square = lambda number: number * number

print(square(5))


developers = [
    {"name": "Alice", "experience": 5},
    {"name": "Bob", "experience": 12},
    {"name": "Carol", "experience": 3}
]

# The key parameter expects a function.
developers.sort(
    key=lambda developer: developer["experience"]
)

