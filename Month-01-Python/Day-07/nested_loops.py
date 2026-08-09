developers = [
    {
        "name": "Alice",
        "skills": ["Python", "SQL"]
    },
    {
        "name": "Bob",
        "skills": ["C#", "Azure", "SQL"]
    },
    {
        "name": "Carol",
        "skills": ["JavaScript", "Python"]
    }
]

for developer in developers:
    print(developer["name"])

    for skill in developer["skills"]:
        print(f"  - {skill}")

    print()


developers = []

number_of_developers = int(input("How many developers? "))

for _ in range(number_of_developers):
    name = input("Developer name: ")
    language = input("Primary language: ")

    developer = {
        "name": name,
        "language": language
    }

    developers.append(developer)

print(developers)
