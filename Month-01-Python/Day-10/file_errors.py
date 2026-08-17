try:
    with open("does_not_exist.txt", "r", encoding="utf-8") as file:
        contents = file.read()
except FileNotFoundError:
    print("The requested file does not exist.")


import os
print(os.getcwd())


from pathlib import Path
file_path = Path("developers.txt")
print(file_path)

if file_path.exists():
    print("The file exists.")
else:
    print("The file does not exist.")


script_directory = Path(__file__).parent
file_path = script_directory / "developers.txt"

print(file_path)
