languages = ["C#", "Python", "JavaScript"]

print(languages)

print(languages[0])
print(languages[1])
print(languages[2])

print(languages[-1]) # print last item in the list
print(languages[-2]) # print secon to last item in the list

languages.append("Java")
print(languages)

languages.remove("JavaScript")
print(languages)

languages[0] = "C# / .NET"
print(languages)

print(len(languages))

for language in languages:
    print(language)

for language in languages:
    print(f"I have {language} in my language list.")

if "Python" in languages:
    print("Python is in the list.")

if "COBOL" not in languages:
    print("COBOL is not in the list.")

numbers = [10, 20, 30, 40, 50]  # arrays are zero-based
print(numbers[1:4])  # range starts at index 1 and ends before index 4
print(numbers[:3]) # everything before the third index
print(numbers[2:]) # the second index and everything after that

# to pre-allocate a list of a specific length before you have the values:
my_list = [None] * 10   # Indexes 0 - 9 will pre-exist
