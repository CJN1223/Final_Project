import random

print("Number Guessing Game")
print("----------------------------------------------------")
print("Choose your difficulty level:")
print("1. Easy (1-100)")
print("2. Medium (1-500)")
print("3. Hard (1-1000)")

difficulty = input("Enter Easy, Medium, or Hard: ")
while difficulty not in ["Easy", "Medium", "Hard"]:
    print("Invalid input. Please enter Easy, Medium, or Hard.")
    difficulty = input("Enter Easy, Medium, or Hard: ")

if difficulty == "Easy":
    max_num = 100
elif difficulty == "Medium":
    max_num = 500
else:
    max_num = 1000

num = random.randint(1, max_num)

attempts = 0
correctGuess = False

while not correctGuess:
    try:
        guess = int(input(f"Enter your guess (1-{max_num}): "))
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