import json
from pathlib import Path

def load_developers(file_path):
    try:
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as file:
                developers = json.load(file)
        else:
            developers = []
    except FileNotFoundError:
        developers = []
    except json.decoder.JSONDecodeError:
        print(f"Could not read {file_path.name}.")
        developers = []

    return developers

def save_developers(file_path, developers):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(developers, file, indent=4)

def list_developers(developers):
    if len(developers) == 0:
        print("No developers have been registered.")
    else:
        print("\nDevelopers")
        print("----------")
        for developer in developers:
            print()
            print(developer["name"])
            print(f'Experience: {developer["experience"]} years')
            print("Skills:")
            for skill in developer["skills"]:
                print(f"- {skill}")

def add_developer(developers):
    skills = []
    name = input("Developer name: ")

    for developer in developers:
        if name.strip().lower() == developer["name"].strip().lower():
            print(f"A developer named {developer["name"]} is already registered.")
            return False

    years = get_integer("Years of experience: ")
    skills_count = get_integer("How many skills? ")
    for _ in range(skills_count):
        skill = input("Enter skill: ")
        skills.append(skill)
    developers.append({
        "name": name,
        "experience": years,
        "skills": skills
    })
    return True

def get_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            break
        except ValueError:
            print("Please enter a whole number.")
    return number

def main():
    file_changed = False
    script_directory = Path(__file__).parent
    file_path = script_directory / "developers.json"

    developers = load_developers(file_path)

    while True:
        print("\nDeveloper Registry")
        print("------------------")
        print()
        print("1. List developers")
        print("2. Add developer")
        print("3. Exit")
        print()
        choice = input("Choice: ")
        if choice == "1":
            list_developers(developers)
        elif choice == "2":
            if add_developer(developers):
                file_changed = True
        elif choice == "3":
            break

    if file_changed:
        save_developers(file_path, developers)


if __name__ == "__main__":
    main()
