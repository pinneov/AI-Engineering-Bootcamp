languages = {"Python", "C#", "JavaScript"}  # sets are lists of unique values - declared as dictionary without values for the keys
print(languages)

languages.add("Java")
languages.add("Python")  # does nothing because "Python" is already in the list
print(languages)

# remove duplicates from list by converting to set
languages = [
    "Python",
    "C#",
    "Python",
    "JavaScript",
    "C#",
    "Python"
]

unique_languages = set(languages)  # convert list to set
print(unique_languages)

languages = list(unique_languages)  # convert set to list - do not count on the order of items from a set
print(languages)
