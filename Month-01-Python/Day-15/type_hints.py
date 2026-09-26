name: str = "Alice"
experience: int = 5
active: bool = True
developers: list[dict] = []

# Still allowed (type hints are not enforced):
experience = "five"

names: list[str]
scores: dict[str, int]
skills: set[str]
coordinates: tuple[float, float]

developers: list[dict[str, object]]


# Union Types

def find_developer(name: str) -> str | None:  # returns str OR None
    return None

# value may be str OR int
def parse_id(value: str | int) -> int:
    return int(value)


from typing import Optional

def find_developer(name: str) -> Optional[str]:  # means it returns: str | None
    return None

# The argument is still required
def display(name: str | None):
    pass

display()       # error
display(None)   # allowed by the annotation


def display(name: str | None = None):
    pass

display()       # allowed now and defaults to None


from typing import Any

value: Any     # No type-checking, custom functions can be called on it even though the type is not declared
value: object  # type checking is performed and requires that only functions that belong to the object base class can be called.


myDict = dict[str, str | int | list[str]]  # Value of each entry can be a string, a number, or a list of strings

type DeveloperData = dict[
    str,
    str | int | list[str]
]

def display(developer: DeveloperData) -> None:
    pass

