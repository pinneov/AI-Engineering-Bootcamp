import string_utils

def add_unique_skill(skills, skill):
    if skill is None or skill.strip() == "":
        return
    clean_skill = string_utils.normalize_skill(skill)
    if clean_skill not in skills:
        skills.append(clean_skill)

def print_developer(developer):
    string_utils.display_title("Developer Profile")
    print(f"Name: {developer["name"]}")
    print("\nSkills:")
    for skill in developer["skills"]:
        print(f"- {skill}")
    print(f"\nTotal unique skills: {len(developer["skills"])}")
