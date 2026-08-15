def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

    if age > 120:
        raise ValueError("Age cannot be greater than 120.")

    return age

try:
    age = int(input("Enter your age: "))
    validated_age = validate_age(age)
except ValueError as ex:
    print(f"Invalid age: {ex}")
else:
    print(f"Accepted age: {validated_age}")
