developer = {
    "name": "Alice",
    "languages": ["Python", "C#", "SQL"],
    "certifications": ["Azure AI", "AWS"]
}

print(developer["name"])
print(developer["languages"])

print(developer["languages"][0])

print(developer["certifications"][1])

print(f"{developer['name']}'s languages:")
for language in developer["languages"]:
    print(f"- {language}")

developer = {
    "name": "Alice",
    "skills": [
        {
            "name": "Python",
            "level": "Advanced"
        },
        {
            "name": "C#",
            "level": "Intermediate"
        },
        {
            "name": "SQL",
            "level": "Advanced"
        }
    ]
}

print(developer["skills"][0]["name"])
print(developer["skills"][1]["level"])
