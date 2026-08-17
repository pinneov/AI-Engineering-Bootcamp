name = input("Developer name: ")

with open("developers.txt", "a") as file:
    file.write(name + "\n")


# with open("developers.txt", "w", encoding="utf-8") as file:

