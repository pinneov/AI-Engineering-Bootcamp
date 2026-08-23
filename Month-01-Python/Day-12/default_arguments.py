def create_developer(name, active=True):
    print(f"Name: {name}")
    print(f"Active: {active}")


create_developer("Alice")
create_developer("Bob", False)


# Defaults are created when the function is defined, not every time the function is called - so mutable types mat get changed

def add_skill(skill, skills=[]):
    skills.append(skill)
    return skills

print(add_skill("Python"))  #  ['Python']             
print(add_skill("C#"))      #  ['Python', 'C#']             


# Use this pattern instead to make each call that omits skills create a fresh list.

def add_skill(skill, skills=None):
    if skills is None:
        skills = []

    skills.append(skill)
    return skills

print(add_skill("Python"))  #  ['Python']             
print(add_skill("C#"))      #  ['C#']             
