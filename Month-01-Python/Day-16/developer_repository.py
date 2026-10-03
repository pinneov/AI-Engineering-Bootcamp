from dataclasses import dataclass, field
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


class MemoryRepository[T]:
    def __init__(self):
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def get_all(self) -> list[T]:
        return self._items.copy()


from typing import Protocol, runtime_checkable

class DeveloperRepository(Protocol):
    def find(self, name: str) -> Developer | None:
        pass

    def get_all(self) -> list[Developer]:
        pass

@runtime_checkable
class Named(Protocol):
    @property
    def name(self) -> str:
        pass


class MemoryDeveloperRepository:
    def __init__(self):
        self._repo: MemoryRepository[Developer] = MemoryRepository[Developer]()

    def add(self, item: Developer) -> None:
        self._repo.add(item)

    def get_all(self) -> list[Developer]:
        return self._repo.get_all()

    def find(self, name: str) -> Developer | None:
        for developer in self._repo.get_all():
            if developer.name == name:
                return developer

        return None
    

class MemoryDeveloperRepository2(MemoryRepository[Developer]):
    def find(self, name: str) -> Developer | None:
        for developer in self.get_all():
            if developer.name == name:
                return developer

        return None
    

def print_repository(repository: DeveloperRepository) -> None:
    for developer in repository.get_all():
        print(developer)

def first_or_none[T](values: list[T]) -> T | None:
    if len(values) > 0:
        return values[0]

    return None

def print_developer(repository: DeveloperRepository, name: str) -> None:
    developer = repository.find(name)
    if developer is not None:
        print(developer)
    
def main():

    repo = MemoryDeveloperRepository()
    repo.add(Developer("Alice", 5))
    repo.add(Developer("Jake", 11))
    print_repository(repo)

    repo2 = MemoryDeveloperRepository2()
    repo2.add(Developer("Alice", 5))
    repo2.add(Developer("Jake", 11))
    print_repository(repo2)


    print(first_or_none(['One', 'Two', 'Three']))

    print(first_or_none(repo.get_all()))

    print_developer(repo, "Alice")
    print_developer(repo2, "Alice")

    developers = repo.get_all()
    developers.clear()

    developers2 = repo.get_all()

    print(len(developers))
    print(len(developers2))

    developers2[0].add_skill("Python")

    developers3 = repo.get_all()

    print(developers3[0])

    developer = first_or_none(repo.get_all())

    if developer is not None:
        if isinstance(developer, Named):
            print(developer.name)

        

if __name__ == "__main__":
    main()
    