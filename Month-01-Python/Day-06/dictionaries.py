developer = {
    "name": "Vincent",
    "language": "C#",
    "learning": "Python"
}

print(developer["name"])
print(developer["language"])

developer = {
    "name": "Vincent",              # str
    "years_experience": 22,         # int
    "is_learning_ai": True,         # bool
    "languages": ["C#", "Python"]   # list
}

print(developer)

# add a key
developer["city"] = "Los Angeles"
print(developer)

# modify a value
developer["is_learning_ai"] = "AI Engineering"
print(developer)

# remmove a value
developer.pop("city")
print(developer)

# iterating keys
for key in developer:
    print(key)

# iterating key/value pairs
for key, value in developer.items():
    print(f"{key}: {value}")

# key doesn't exist
#print(developer["favorite_food"])  ### KeyError
print(developer.get("favorite_food"))  # returns "None"
print(developer.get("favorite_food", "Not specified")) # provide default, returns "Not specified"

