developer = {
    "name": input("Developer name: "),
    "skills": []
}

number_of_skills = int(input("How many skills would you like to enter? "))

#skill_number = 0

#while skill_number < number_of_skills:
#for skill_number in range(0, number_of_skills):
#for skill_number in range(number_of_skills):  # simplified: default is to start at 0
for _ in range(number_of_skills):  # simplified futher: because the variable is never used (_ is Python convention for this)
    developer["skills"].append(input("Enter skill: "))
#    skill_number += 1

print("\nDeveloper Profile")
print("-" * 17)
print(f"Name: {developer['name']}")
print("\nSkills:")
for skill in developer["skills"]:
    print(f"- {skill}")
print(f"\nTotal skills: {len(developer['skills'])}")


# Bonus Challenge
print("\nBonus Challenge 1")
print("-" * 17)
print(f"Name: {developer['name']}")
print("\nSkills:")
unique_skills = set(developer["skills"])
for skill in unique_skills:
    print(f"- {skill}")
print(f"\nTotal skills: {len(unique_skills)}")

print("\nBonus Challenge 2")
print("-" * 17)
print(f"Name: {developer['name']}")
print("\nSkills:")
unique_skills = []
for skill in developer["skills"]:
    if skill not in unique_skills:
        unique_skills.append(skill)
for skill in unique_skills:
    print(f"- {skill}")
print(f"\nTotal skills: {len(unique_skills)}")
