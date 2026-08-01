name = input("What is your name? ")
age = int(input("How old are you? "))
fav_programming_lang = input("What is your favorite programming language? ")
years_experience = int(input("How many years of experience do you have? "))
next_year_exp = years_experience + 1

print("\nDeveloper Profile")
print("-" * 20)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Favorite Language: {fav_programming_lang}")
print(f"Experience: {years_experience} years")
print(f"Next year you will have {next_year_exp} years of experience.")
