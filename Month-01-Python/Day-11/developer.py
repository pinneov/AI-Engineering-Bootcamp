class Developer:
    def __init__(self, name, years_experience):
        self.name = name
        self.years_experience = years_experience
        self.skills = []

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)

    def display(self):
        print(self.name)
        print(f"Experience: {self.years_experience} years")
        print("Skills:")

        for skill in self.skills:
            print(f"- {skill}")

    def to_dict(self):
        return {
            "name": self.name,
            "experience": self.years_experience,
            "skills": self.skills
        }



developer1 = Developer("Alice", 5)
developer2 = Developer("Bob", 10)

print(developer1.name)
print(developer2.name)

developer = Developer("Vincent", 22)

developer.add_skill("C#")
developer.add_skill("Python")
developer.add_skill("Python")

print(developer.skills)
developer.display()

data = developer.to_dict()
print(data)

# Static typing is not enforced, but adding it helps tools:

# class Developer:
#     def __init__(self, name: str, years_experience: int):
#         self.name = name
#         self.years_experience = years_experience
#         self.skills: list[str] = []

#     def add_skill(self, skill: str) -> None:
#         if skill not in self.skills:
#             self.skills.append(skill)

#def get_name(developer: Developer) -> str:
#    return developer.name

