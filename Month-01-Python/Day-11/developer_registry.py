import json
from pathlib import Path

class Person:
    def __init__(self, name: str):
        self.name = name

class Developer(Person):
    def __init__(self, name: str, years_experience: int):
        super().__init__(name)
        self.years_experience = years_experience
        self.skills: list[str] = []

    def __str__(self) -> str:
        return f"{self.name} ({self.years_experience} years)"

    def add_skill(self, skill: str) -> None:
        if skill not in self.skills:
            self.skills.append(skill)

    def display(self) -> None:
        print(self.name)
        print(f"Experience: {self.years_experience} years")
        print("Skills:")
        for skill in self.skills:
            print(f"- {skill}")

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "experience": self.years_experience,
            "skills": self.skills
        }

    from typing import Self
    @classmethod
    def from_dict(cls, data: dict) -> Self:
        developer = cls(
            data["name"],
            data["experience"]
        )
        for skill in data["skills"]:
            developer.add_skill(skill)
        return developer

    @classmethod
    def c_from_dict(cls, data: dict) -> Developer:
        developer = cls(
            data["name"],
            data["experience"]
        )
        for skill in data["skills"]:
            developer.add_skill(skill)
        return developer

    @staticmethod
    def s_from_dict(data: dict) -> Developer:
        developer = Developer(
            data["name"],
            data["experience"]
        )
        for skill in data["skills"]:
            developer.add_skill(skill)
        return developer


def load_developers(file_path: Path) -> list[Developer]:
    developers: list[Developer] = []

    try:
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as file:
                developers_dict = json.load(file)
        else:
            developers_dict: list[dict] = []
    except FileNotFoundError:
        developers_dict: list[dict] = []
    except json.decoder.JSONDecodeError:
        print(f"Could not read {file_path.name}.")
        developers_dict: list[dict] = []

    for developer_dict in developers_dict:
        developers.append(Developer.from_dict(developer_dict))

    return developers

def save_developers(file_path: Path, developers: list[Developer]) -> None:
    developers_dict: list[dict] = []
    for developer in developers:
        developers_dict.append(developer.to_dict())

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(developers_dict, file, indent=4)

def list_developers(developers: list[Developer]) -> None:
    if len(developers) == 0:
        print("No developers have been registered.")
    else:
        print("\nDevelopers")
        print("----------")
        for developer in developers:
            print()
            developer.display()

def add_developer(developers: list[Developer]) -> bool:
    name = input("Developer name: ")

    for developer in developers:
        if name.strip().lower() == developer.name.strip().lower():
            print(f"A developer named {developer.name} is already registered.")
            return False

    years = get_integer("Years of experience: ")

    developer = Developer(name, years)

    skills_count = get_integer("How many skills? ")
    for _ in range(skills_count):
        skill = input("Enter skill: ")
        developer.add_skill(skill)
    developers.append(developer)
    return True

def get_integer(prompt) -> int:
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
        choice = get_integer("Choice: ")
        if choice == 1:
            list_developers(developers)
        elif choice == 2:
            if add_developer(developers):
                file_changed = True
        elif choice == 3:
            break

    if file_changed:
        save_developers(file_path, developers)


if __name__ == "__main__":
    main()
