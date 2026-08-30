numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number * number)

# Same thing:
squares = [
    number * number
    for number in numbers
]

squares = [number * number for number in numbers]

######################################################

evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)

# Same thing:
evens = [
    number
    for number in numbers
    if number % 2 == 0
]

######################################################

developers = [
    {"name": "Alice", "experience": 5},
    {"name": "Bob", "experience": 12},
    {"name": "Carol", "experience": 3}
]

experienced = [
    developer
    for developer in developers
    if developer["experience"] >= 5
]

names = [
    developer["name"]
    for developer in developers
]

######################################################

developers = [
    {"name": "Alice", "experience": 5},
    {"name": "Bob", "experience": 12},
    {"name": "Carol", "experience": 3}
]

# Convert to Dictionary:
experience_by_name = {
    developer["name"]: developer["experience"]
    for developer in developers
}

######################################################

skills = ["Python", "SQL", "Python", "C#", "SQL"]

# Convert to Set:
unique_skills = {
    skill
    for skill in skills
}

######################################################

#  [x for x in values]             # list

#  {x for x in values}             # set

#  {x: something for x in values}  # dictionary

######################################################

# Nested

developers = [
    {
        "name": "Alice",
        "skills": ["Python", "SQL"]
    },
    {
        "name": "Bob",
        "skills": ["C#", "SQL"]
    }
]

skills = [
    skill
    for developer in developers
    for skill in developer["skills"]
]

#  ["Python", "SQL", "C#", "SQL"]

######################################################

# Interators

numbers = [10, 20, 30]  # List is Iterable

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

next(iterator)  # Fourth time raises StopIteration

######################################################

