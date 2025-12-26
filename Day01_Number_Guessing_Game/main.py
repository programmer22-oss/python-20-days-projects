import random

# Step 1: Computer selects a random number
secret_number = random.randint(1, 100)

attempts = 0

print("🎯 Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too high! Try again.")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
        break
