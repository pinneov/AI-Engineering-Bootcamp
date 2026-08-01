years = int(input("Years of programming experience: "))

if years >= 10:
    print("Senior Developer")
elif years >= 5:
    print("Mid-Level Developer")
elif years >= 1:
    print("Junior Developer")
else:
    print("Beginner")
