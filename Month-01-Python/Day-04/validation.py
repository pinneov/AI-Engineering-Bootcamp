#age = int(input("Enter your age: "))
#
#while age < 0 or age > 120:
#    print("Please enter an age from 0 through 120.")
#    age = int(input("Enter your age again: "))
#
#print(f"Accepted age: {age}")


while True:
    age = int(input("Enter your age: "))

    if 0 <= age <= 120:
        break

    print("Please enter an age from 0 through 120.")

print(f"Accepted age: {age}")
