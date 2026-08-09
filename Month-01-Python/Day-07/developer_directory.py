developers = []

number_of_developers = int(input("How many developers would you like to enter? "))

for _ in range(number_of_developers):
    name = input("Developer name: ")
    experience_years = int(input("Years of experience: "))
    skill_count = int(input("How many skills? "))
    skills = []

    for _ in range(skill_count):
        skills.append(input("Enter skill: "))

    developers.append(
        {
            "name": name,
            "years": experience_years,
            "skills": skills
        }
    )

print("Developer Directory")
print("-" * 19)

for developer in developers:
    print(f"\n{developer["name"]}")
    print(f"Experience: {developer["years"]} years")
    print("Skills:")
    for skill in developer["skills"]:
        print(f"- {skill}")

print(f"\nTotal developers: {len(developers)}")

skill_to_search = input("Search for skill: ").strip()

print("\nCase-sensitive matches:")
print(f"Developers with {skill_to_search}:")
for developer in developers:
    if skill_to_search in developer["skills"]:
        print(f"- {developer["name"]}")

print("\nCase-insensitive matches:")
print(f"Developers with {skill_to_search}:")
for developer in developers:
    has_skill = False
    for skill in developer["skills"]:
        if skill_to_search.lower() == skill.lower():
            has_skill = True
            break
    if has_skill:
        print(f"- {developer["name"]}")

most_experienced_developer = { "name": "No developer", "years": -1, "skills": [] }

for developer in developers:
    if developer["years"] > most_experienced_developer["years"]:
        most_experienced_developer = developer

print("Most Experienced Developer")
print("-" * 26)
print(f"{most_experienced_developer["name"]} - {most_experienced_developer["years"]} years")

total_skills = 0

for developer in developers:
    total_skills += len(developer["skills"])

print(f"Total skills across all developers: {total_skills}")
