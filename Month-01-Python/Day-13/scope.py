def calculate():
    result = 10 + 5
    print(result)


calculate()

########################################

message = "Global"

def outer():
    message = "Enclosing"

    def inner():
        message = "Local"
        print(message)

    inner()
    print(message)


outer()
print(message)

########################################

count = 10

def increment():
    global count  # use a variable from module/global scope

    count += 1


increment()
print(count)

########################################

def outer():
    count = 0

    def increment():
        nonlocal count  # use a variable from an enclosing function
        count += 1

    increment()
    print(count)


outer()