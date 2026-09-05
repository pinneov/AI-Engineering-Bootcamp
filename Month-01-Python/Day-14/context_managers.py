class Operation:
    def __enter__(self):
        print("Starting operation")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Ending operation")

with Operation() as operation:  # operation is assigned to whatever __enter__() returns
    print("Doing work")

#with Operation():
#    raise ValueError("Something failed")
    # Then, unless __exit__() explicitly suppresses the exception, the exception continues propagating.

#######################################

from contextlib import contextmanager

@contextmanager
def operation():
    print("Starting operation")

    try:
        yield  # Executes the with block
    finally:
        print("Ending operation")


with operation():  # no need for an "as" because no value is yielded
    print("Doing work")

#######################################

# yield can also return something:

@contextmanager
def operation():
    print("Starting")

    resource = "My resource"

    try:
        yield resource  # This is like returning a value from __enter__ on a class
    finally:
        print("Ending")

with operation() as resource:  # yielded value becomes the variable
    print(resource)

#######################################
# Common uses for decorators:
# logging
# timing
# authorization
# validation
# retry behavior
# caching
# metrics

