username = input("Username: ").strip().lower()
password = input("Password: ")

if username == "vincent" and password == "python123":
    print("Access Granted")
elif username != "vincent":
    print("Unknown user")
else:
    print("Incorrect password")
