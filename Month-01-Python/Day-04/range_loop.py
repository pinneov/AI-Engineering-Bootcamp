# range(stop) start defaults to zero
for number in range(5):
    print(number)

print("\n")

# range(start, stop)
for number in range(1, 6):
    print(number)

print("\n")

# range(start, stop, step)
for number in range(2, 11, 2):
    print(number)


number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")
