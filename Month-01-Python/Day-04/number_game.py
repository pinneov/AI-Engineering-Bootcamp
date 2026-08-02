secret_number = 7
guess = 0
attempts = 0

while guess != secret_number:
    guess = int(input("Guess a number from 1 to 10: "))

    if guess < 1 or guess > 10:
        print("Your guess must be between 1 and 10.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print(f"Correct! You needed {attempts} attempts.")
