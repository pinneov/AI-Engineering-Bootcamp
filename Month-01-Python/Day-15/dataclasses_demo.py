from dataclasses import dataclass


@dataclass
class Developer:
    name: str
    experience: int

# Auto generated:
# __init__   Assigns the field values
# __repr__   Converts to string representation
# __eq__     Does Value comparison of all fields

developer = Developer("Alice", 5)

print(developer)  # Developer(name='Alice', experience=5)


developer1 = Developer("Alice", 5)
developer2 = Developer("Alice", 5)

print(developer1 == developer2)  # True (has same values)
print(developer1 is developer2)  # False (does not point to the same instance)

@dataclass
class Developer:
    name: str
    experience: int = 0  # Default value makes this an optional field in the constructor - optional fields must be defined after required fields

developer = Developer("Alice")
developer = Developer("Alice", 5)


from dataclasses import dataclass, field

@dataclass
class Developer:
    name: str
    skills: list[str] = field(default_factory=list)  # default_factory=list means: Call list() separately when each new Developer needs its default value.

field(default_factory=dict)
field(default_factory=set)



@dataclass
class Developer:
    name: str
    experience: int

    def __post_init__(self):  # initialization logic after the generated __init__()
        if self.experience < 0:
            raise ValueError("Experience cannot be negative.")



# Computed field

from dataclasses import dataclass, field


@dataclass
class Developer:
    name: str
    experience: int
    senior: bool = field(init=False)  # Exclude the field from the constructor

    def __post_init__(self):
        self.senior = self.experience >= 10

developer = Developer("Alice", 12)

print(developer.senior)  # True

@dataclass(frozen=True)  # Immutable-like (cannot change the field assignments after constructor - contents of objects assigned can still be changed)
class Coordinate:
    x: float
    y: float

coordinate = Coordinate(10, 20)
coordinate.x = 30 # ERROR - raises dataclasses.FrozenInstanceError

