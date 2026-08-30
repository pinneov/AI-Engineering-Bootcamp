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

empty_set = set()   # Creates an empty set <class 'set'>
empty_dict = {}     # Creates an empty dictionary <class 'dict'>
empty_list = []
empty_tuple = () # or tuple()
one_item_tuple = (1,)  # Must have at least one comma in a non-empty tuple - use trailing comma

new_set = {1, 2, 3, 4}
new_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4}
new_list = [1, 2, 3, 4]
new_tuple = (1, 2, 3, 4)

