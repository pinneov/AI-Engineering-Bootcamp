from dataclasses import dataclass, field, FrozenInstanceError
from enum import Enum

class DeveloperLevel(Enum):
    JUNIOR = "Junior"
    MID_LEVEL = "Mid-Level"
    SENIOR = "Senior"

@dataclass
class Developer:
    name: str
    experience: int
    skills: list[str] = field(default_factory=list)
    level: DeveloperLevel = field(init=False)

    def __post_init__(self):
        if self.experience < 0:
            raise ValueError(
                "Experience cannot be negative."
            )

        if self.experience >= 10:
            self.level = DeveloperLevel.SENIOR
        elif self.experience >= 5:
            self.level = DeveloperLevel.MID_LEVEL
        else:
            self.level = DeveloperLevel.JUNIOR

    def has_skill(self, skill: str) -> bool:
        for existing_skill in self.skills:
            if existing_skill.lower() == skill.lower():
                return True
        return False

    def add_skill(self, skill: str) -> None:
        if self.has_skill(skill) == False:
            self.skills.append(skill)

@dataclass(frozen=True)
class ProjectAssignment:
    developer_name: str
    project_name: str
    hourly_rate: float

def main():

    def find_developer(developers: list[Developer], name: str) -> Developer | None:

        for developer in developers:
            if developer.name.lower() == name.lower():
                return developer

        return None

    def developers_at_level(developers: list[Developer], level: DeveloperLevel) -> list[Developer]:
        return [
            developer
            for developer in developers
            if developer.level == level
        ]

    developer1 = Developer("Alice", 5)
    developer2 = Developer("Alice", 5)

    print(f"Developers are equal: {developer1 == developer2}")
    print(f"Developers are same instance: {developer1 is developer2}")
    
    developer1.add_skill("C#")

    if len(developer1.skills) > 0:
        for skill in developer1.skills:
            print(f"Developer 1 Skill: {skill}")
    else:
        print("Developer 1 has no skills.")

    if len(developer2.skills) > 0:
        for skill in developer2.skills:
            print(f"Developer 2 Skill: {skill}")
    else:
        print("Developer 2 has no skills.")

    assignment1 = ProjectAssignment("Vincent", "Bootcamp", 100.00)

    try:
        assignment1.hourly_rate = 200.00
    except FrozenInstanceError:
        print("Changes are not permitted!")

    

        

if __name__ == "__main__":
    main()
    