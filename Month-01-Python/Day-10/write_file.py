file = open("developers.txt", "w")

file.write("Alice\n")
file.write("Bob\n")
file.write("Carol\n")

file.close()


with open("developers.txt", "w") as file:
    file.write("Alice\n")
    file.write("Bob\n")
    file.write("Carol\n")
    print(file.closed)

print(file.closed)


developers = [
    {
        "name": "Alice",
        "years": 5,
        "skills": ["Python", "SQL"]
    },
    {
        "name": "Bob",
        "years": 10,
        "skills": ["C#", "Azure"]
    }
]

import json

with open("developers.json", "w", encoding="utf-8") as file:
    #json.dump(developers, file)
    json.dump(developers, file, indent=4)

with open("developers.json", "r", encoding="utf-8") as file:
    developers = json.load(file)
