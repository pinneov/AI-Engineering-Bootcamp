try:
    number = int(input("Enter a number: "))
    print(f"You entered {number}.")
except ValueError:
    print("Invalid number.")
finally:  # executes no matter what - clean run, error, or early return.
    print("This always runs.")
