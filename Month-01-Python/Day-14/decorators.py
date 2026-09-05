def log_call(function):
    def wrapper():
        print("Before function")

        function()

        print("After function")

    return wrapper


def say_hello():
    print("Hello!")

say_hello = log_call(say_hello)  # Replace the function with a wrapper around the original function

say_hello()

#########################################

# Equivilent using decorator syntax:
# Replaces the defined function with a call to the function name after the @ sign, passing the defined function as a parameter

@log_call
def say_hello():
    print("Hello!")

#########################################

@classmethod
def from_dict(cls, data):
    pass

# is equivilent to:

def from_dict(cls, data):
    pass

from_dict = classmethod(from_dict)

#########################################
# A well-behaved wrapper usually needs to forward both the arguments and the return value.
# To be able to pass arguments:

def log_call(function):
    def wrapper(*args, **kwargs):
        print("Before function")

        result = function(*args, **kwargs)  # return B to here

        print("After function")

        return result   # return C from here

    print("Returning wrapper")
    return wrapper  # return A from here

print("Defining wrapper")

@log_call  # log_call function is called here and its return value is stored as "add" variable
def add(a, b):  # return A to here
    return a + b   # return B from here

print("Calling wrapper")

# args = (10, 5), kwargs = {}
result = add(10, 5)  # return C to here

print(f"Result is {result}")

#########################################

def greet(name):
    """Greets a person."""
    print(f"Hello, {name}")

print(greet.__name__)  # greet
print(greet.__doc__)   # Greets a person.

#########################################

@log_call
def greet(name):
    """Greets a person."""
    print(f"Hello, {name}")

print(greet.__name__)  # wrapper
print(greet.__doc__)   # None

#########################################

from functools import wraps

def log_call(function):
    @wraps(function)   # copies important metadata from the wrapped function to the wrapper.
    def wrapper(*args, **kwargs):
        print("Before function")

        result = function(*args, **kwargs)

        print("After function")

        return result

    return wrapper

@log_call
def greet(name):
    """Greets a person."""
    print(f"Hello, {name}")

print(greet.__name__)  # greet
print(greet.__doc__)   # Greets a person.
