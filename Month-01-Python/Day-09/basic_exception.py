while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid whole number.")

print(f"You are {age} years old.")

# To catch all errors - this is bad practice, only catch the types we know how to handle
#except:

# To catch all errors of type Exception - this is too broad, also bad practice
#except Exception:

#try:
#    age = int(input("Enter your age: "))
#except ValueError as ex:
#    print("Invalid age.")
#    print(f"{type(ex).__name__}: {ex}")

