def main():

    from functools import wraps

    def log_call(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print(f"Calling: {function.__name__}")
            result = function(*args, **kwargs)
            print(f"Finished: {function.__name__}")
            return result
        return wrapper

    @log_call
    def say_hello():
        print("Hello!")

    @log_call
    def greet(name):
        print(f"Hello {name}!")

        if name == "Vincent":
            is_developer = True
        else:
            is_developer = False

        return is_developer

    say_hello()

    for _ in range(2):
        name = input("Enter your name: ")
        is_developer = greet(name)
        if is_developer == True:
            print("You are a developer!")


    from time import perf_counter
    
    def measure_time(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            start = perf_counter()
            result = function(*args, **kwargs)
            end = perf_counter()
            print(f"{end - start} seconds elapsed")
            return result
        return wrapper

    @log_call
    @measure_time
    def get_age():
        age = int(input("Enter your age: "))
        return age

    @measure_time
    @log_call
    def get_favorite_color():
        color = input("Enter your favorite color: ")
        return color

    age = get_age()
    color = get_favorite_color()

    print(f"You are {age} years old and your favorite color is {color}")

    def require_minimum_experience(years):
        def decorator(function):
            @wraps(function)
            def wrapper(developer, *args, **kwargs):
                if developer["experience"] >= years:
                    return function(developer, *args, **kwargs)
                else:
                    print("Developer does not have enough experience")
                    return None
            return wrapper
        return decorator

    @require_minimum_experience(5)
    def assign_project(developer, project):
        developer["projects"].append(project)
        price = 100 * developer["experience"]
        return price

    developers = [
        {
            "name": "Vincent",
            "experience": 22,
            "projects": []
        },
        {
            "name": "Jake",
            "experience": 3,
            "projects": []
        }
    ]

    price = assign_project(developers[0], "ProjectA")
    if price is not None:
        print(f"ProjectA will cost {price}")

    price = assign_project(developers[1], "ProjectB")
    if price is not None:
        print(f"ProjectB will cost {price}")
    
    class DeveloperSession:
        developer = None

        def __init__(self, developer):
            self.developer = developer

        def __enter__(self):
            print(f"Opening session for {self.developer["name"]}")
            return self

        def __exit__(self, exc_type, exc, tb):
            print(f"Closing session for {self.developer["name"]}")

    with DeveloperSession(developers[0]) as session:
        print(f"Working on session for {session.developer["name"]}")

    try:
        with DeveloperSession(developers[1]) as session:
            raise ValueError("Test Failure")
    except ValueError as ex:
        print(f"Error in main: {ex}")


    from contextlib import contextmanager

    @contextmanager
    def developer_session(developer):
        print(f"Opening session for {developer["name"]}")
        try:
            yield
        finally:
            print(f"Closing session for {developer["name"]}")

    try:
        with developer_session(developers[0]):
            raise ValueError("Test Failure Two")
    except ValueError as ex:
        print(f"Error in main: {ex}")


if __name__ == "__main__":
    main()
