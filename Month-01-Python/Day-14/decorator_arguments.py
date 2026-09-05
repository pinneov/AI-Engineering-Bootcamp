from functools import wraps

def repeat(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = None

            for _ in range(times):
                result = function(*args, **kwargs)

            return result

        return wrapper

    return decorator

@repeat(3)
def say_hello():
    print("Hello")

say_hello()

# decorator remembers times
# wrapper remembers function
# wrapper can also access times from the enclosing scope

##########################################

def decorator_a(function):
    pass

def decorator_b(function):
    pass

# multiple decorators are processed from the bottom up
@decorator_a
@decorator_b
def process():
    pass

# original process
#        ↓
#  decorator_b
#        ↓
#  decorator_a
#        ↓
# final process


# same thing as:
process = decorator_a(
    decorator_b(process)
)

