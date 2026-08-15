try:
    number1 = int(input("First number: "))
    number2 = int(input("Second number: "))

    result = number1 / number2

except ValueError:
    print("Both values must be whole numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:  #  Only executes if no exceptions were caught.  This this if you are calling additional code that you do want want the above handlers to accidentally catch.
    print(result)

print(isinstance(ValueError(), Exception))         # True
print(isinstance(ZeroDivisionError(), Exception))  # True
