developers = [
    {
        "name": "Alice",
        "language": "Python",
        "years": 5
    },
    {
        "name": "Bob",
        "language": "C#",
        "years": 10
    },
    {
        "name": "Carol",
        "language": "Javascript",
        "years": 3
    }
]

print(developers)
print(developers[0])
print(developers[0]["name"])

print(developers[1]["language"])
print(developers[2]["years"])
print(developers[-1]["name"])

for developer in developers:
    print(developer)

for developer in developers:
    print(f"{developer['name']} uses {developer['language']}.")

for developer in developers:
    if developer["years"] >= 5:
        print(f"{developer['name']} has at least 5 years of experience.")

for developer in developers:
    if developer["language"] == "Python":
        print(f"Python developer found: {developer['name']}")

