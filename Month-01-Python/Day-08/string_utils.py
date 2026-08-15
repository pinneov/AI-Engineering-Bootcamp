def normalize_name(name):
    return name.strip().title()

def normalize_skill(skill):
    return skill.strip().lower()

def display_title(title):
    print(f"\n{title}")
    print("-" * len(title))

def normalize_yes_no(value):
    if value is None:
        return None
    clean_value = value.strip().lower()
    if clean_value == "yes" or clean_value == "y":
        return True
    else:
        return False
