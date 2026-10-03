from typing import Protocol


class DeveloperRepository(Protocol):
    def find(
        self,
        name: str
    ) -> Developer | None:
        ...

    def get_all(self) -> list[Developer]:
        ...


def print_developers(
    repository: DeveloperRepository
) -> None:

    for developer in repository.get_all():
        print(developer.name)



