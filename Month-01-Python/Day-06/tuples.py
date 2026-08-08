coordinates = (34.05, -118.25)
print(coordinates)

print(coordinates[0])
print(coordinates[1])

# tuples are immutable
#coordinates[0] = 40.0   ### typeError

#unpacking a tuple:
testOne, testTwo = ("One", "Two")
print(testOne)
print(testTwo)

def get_developer():
    return "Vincent", "C#"

name, language = get_developer() #tuple returned by function and unpacked by caller
print(name)
print(language)

def get_second_dev():
    return ("Alan", "Tester")  # traditional tuple syntax also supported

nameTwo, occupation = get_second_dev()

print(nameTwo)
print(occupation)

result_var = get_developer()
print(result_var)

def get_third_dev():
    return "One", "Two", "Three"

#one, two = get_third_dev()  # ValueError - value count mismatch
#one, two, three, four = get_third_dev()  # ValueError - value count mismatch
one, two, three = get_third_dev()

print(one)
print(two)
print(three)

full = get_third_dev()  # value count mismatch is allowed if going to a single variable, in which case the entire tuple is assigned
print(full)

two = get_developer()[1]
print(two)
