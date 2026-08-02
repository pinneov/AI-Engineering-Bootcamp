def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temp = float(input("Temperature in Fahrenheit: "))

celsius = fahrenheit_to_celsius(temp)

print(f"{temp} F = {celsius:.2f} C")
