def main():

    def developers_with_minimum_experience(
        developers,
        minimum_experience
    ):
        for developer in developers:
            if developer["experience"] >= minimum_experience:
                yield developer

    def developers_with_skill(developers, skill):
        for developer in developers:
            for dev_skill in developer["skills"]:
                if skill.strip().lower() == dev_skill.strip().lower():
                    yield developer
                    break


    developers = [
        {"name": "Alice", "experience": 5, "skills": ["Python", "SQL"]},
        {"name": "Bob", "experience": 12, "skills": ["C#", "SQL"]},
        {"name": "Carol", "experience": 3, "skills": ["Perl", "Javascript"]},
        {"name": "Vincent", "experience": 22, "skills": ["C#", "Javascript", "Python", "SQL"]},
        {"name": "Jake", "experience": 1, "skills": ["Python", "Javascript"]},
        {"name": "Mark", "experience": 26, "skills": ["SQL", "Perl", "Cobol"]}
    ]

    experienced = developers_with_minimum_experience(developers, 5)

    python_developers = developers_with_skill(experienced, "Python")

    python_dev_names = [developer["name"] for developer in python_developers]

    for developer in python_dev_names:
        print(developer)

    developers_experience = {
        developer["name"]: developer["experience"]
        for developer in developers
    }

    print(developers_experience)

    unique_skills = {
        skill
        for developer in developers
        for skill in developer["skills"]
    }

    print(unique_skills)

    def create_experience_filter(minimum_experience):
        def inner_filter(developers):
            # interate now so that the Print shows the developers not the generator
            # There are a couple ways to do that:
            #   Use a comprehension when you also need to transform or filter (this example does neither).
            #return [developer for developer in developers_with_minimum_experience(developers, minimum_experience)]
            #   Use List() when you just need to convert the generator.
            return list(developers_with_minimum_experience(developers, minimum_experience))

        return inner_filter

    senior_filter = create_experience_filter(10)

    print(senior_filter(developers))

    def create_minimum_experience_predicate(minimum_experience):
        def matches(developer):
            return developer["experience"] >= minimum_experience
        
        return matches

    senior_predicate = create_minimum_experience_predicate(10)
    
    print(senior_predicate(developers[0]))
    print(senior_predicate(developers[1]))

    def create_processed_counter():
        count = 0
        def counter():
            nonlocal count
            count += 1
            return count
        return counter

    counter = create_processed_counter()

    print(counter())
    print(counter())
    print(counter())

if __name__ == "__main__":
    main()
