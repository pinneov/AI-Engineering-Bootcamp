def display_skills(*args):
    print(args)

display_skills("C#", "Python", "SQL")  

# It makes a tuple
# ('C#', 'Python', 'SQL')

# tuple can be interated
def display_skills(*args):
    for skill in args:
        print(skill)


# args can be named anything
def display_skills(*skills):
    for skill in skills:
        print(skill)

# can be combined
def describe_developer(name, *skills):
    print(f"Developer: {name}")

    for skill in skills:
        print(f"- {skill}")

#######################################

# can be used in the other direction too
def display_three_skills(first, second, third):
    print(first)
    print(second)
    print(third)

skills = ["C#", "Python", "SQL"]
display_three_skills(*skills)

#######################################

def display_metadata(**kwargs):
    print(kwargs)

display_metadata(
    city="Phoenix",
    language="C#",
    experience=22
)

#######################################

def display_metadata(**metadata):
    for key, value in metadata.items():
        print(f"{key}: {value}")

display_metadata(
    city="Phoenix",
    language="C#",
    experience=22
)

#######################################

def describe_developer(name, language):
    print(name)
    print(language)

developer = {
    "name": "Vincent",
    "language": "C#"
}

# unpack the dictionary into named parameters
describe_developer(**developer)

#######################################

# standalone * means parameters after it must be supplied by keyword.
def create_developer(name, *, active=True):
    pass

create_developer("Vincent", active=False)  # works
create_developer("Vincent", False) # does not work

#######################################

# standalone / means parameters before it are positional-only.
def calculate(value, /, precision=2):
    pass

calculate(10)  # works
calculate(value=10)  # does not work

#######################################

