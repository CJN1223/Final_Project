import random

print("Number Guessing Game")
print("----------------------------------------------------")

num = random.randint(1, 100)

attempts = 0
correctGuess = False

while not correctGuess:
    try:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1

        if guess > num:
            print("Too high! Try again.")
        elif guess < num:
            print("Too low! Try again.")
        else:
            print("Correct! You won the game!")
            print("Attempts: ", attempts)
            correctGuess = True
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")