import string_utils
import developer_utils as du

def main():
    name = input("What is your name? ")
    skill_count = int(input("How many skills do you have? "))
    unique_skills = []
    for _ in range(skill_count):
        du.add_unique_skill(unique_skills, input("Enter skill: "))
        
    developer = {
        "name": string_utils.normalize_name(name),
        "skills": unique_skills
    }

    du.print_developer(developer)

if __name__ == "__main__":
    main()
