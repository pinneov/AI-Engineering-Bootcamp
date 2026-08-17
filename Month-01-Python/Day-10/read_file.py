#with open("developers.txt") as file:  # read is the default mode
with open("developers.txt", "r") as file:  # This makes the intent explicit
    contents = file.read()  # entire file

print(contents)

with open("developers.txt", "r") as file:
    first_line = file.readline()  # string includes newline ending
    second_line = file.readline()

print(first_line)
print(second_line)


with open("developers.txt", "r") as file:
    lines = file.readlines()  # list of strings which include newline endings

print(lines)



with open("developers.txt", "r") as file:
    for line in file:     # File interator is by line
        print(line.strip())  # remove the newlines since print will add another one


# File modes:
#  "r" Read
#  "w" overwrite/create
#  "a" Append
#  "x" Create (cannot already exist)
#  "rb" read binary
#  "wb" write binary
