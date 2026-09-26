from enum import Enum

class DeveloperLevel(Enum):
    JUNIOR = "Junior"
    MID_LEVEL = "Mid-Level"
    SENIOR = "Senior"

level = DeveloperLevel.SENIOR

print(level.name)   # SENIOR
print(level.value)  # Senior

if level == DeveloperLevel.SENIOR:
    pass

# Not preferable
if level.value == "Senior":
    pass


# When you don't care what underlying value is stored:
from enum import Enum, auto

class Status(Enum):
    ACTIVE = auto()
    INACTIVE = auto()
    SUSPENDED = auto()

status = Status.ACTIVE

