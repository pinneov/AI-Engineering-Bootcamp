def sort_developers(developers:list[dict], *, sort_by:str, descending:bool=False) -> list[dict]:
    return sorted(developers, key=lambda developer:developer[sort_by], reverse=descending)

def has_all_skills(developer:dict, *required_skills:str) -> bool:
    if len(required_skills) == 0:
        return True

    for skill in required_skills:
        if skill not in developer["skills"]:
            return False
        
    return True

def matches(developer:dict, **criteria):
    if len(criteria) == 0:
        return True

    for key, value in criteria.items():
        if developer[key] != value:
            return False

    return True

def filter_developers(developers:list[dict], *required_skills:str, **criteria) -> list[dict]:
    filtered_developers:list[dict] = []
    for developer in developers:
        if has_all_skills(developer, *required_skills) and matches(developer, **criteria):
            filtered_developers.append(developer)
    return filtered_developers

def generate_report(developers:list[dict], *, sort_by:str=None, descending:bool=False) -> None:
    if sort_by is None:
        sorted_developers = developers
    else:
        sorted_developers = sort_developers(developers, sort_by=sort_by, descending=descending)

    print("Developers")
    print("-" * 10)

    for developer in sorted_developers:
        print(f"\n{developer["name"]}")
        print(f"Experience: {developer["experience"]} years")
        print("Skills:")
        for skill in developer["skills"]:
            print(f"- {skill}")

def main():
    developers = [
        {
            "name": "Bob",
            "experience": 1,
            "skills": ["Javascript"]
        },
        {
            "name": "Jane",
            "experience": 12,
            "skills": ["C#", "SQL"]
        },
        {
            "name": "Alice",
            "experience": 5,
            "skills": ["Python", "SQL"]
        },
        {
            "name": "Jake",
            "experience": 8,
            "skills": ["C#", "Javascript", "Python", "SQL"]
        }
    ]

    report_actions = {
        "sort": sort_developers,
        "filter": filter_developers
    }

    sorted_developers = report_actions["sort"](developers, sort_by="experience", descending=True)
    generate_report(sorted_developers)
    
    criteria = {
        "name": "Alice",
        "experience": 5
    }

    required_skills = ["Python", "SQL"]

    filtered_developers = report_actions["filter"](developers, *required_skills, **criteria)
    generate_report(filtered_developers, sort_by="experience", descending=False)


if __name__ == "__main__":
    main()
