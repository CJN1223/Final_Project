import random

print("Number Guessing Game")
print("----------------------------------------------------")

play_again = "yes" # Controls if the game restarts after a game is completed

while play_again.lower() == "yes": # Outer loop to restart the game
    # Difficulty selection
    print("Choose your difficulty level:")
    print("1. Easy (1-100)")
    print("2. Medium (1-500)")
    print("3. Hard (1-1000)")

    # Validate difficulty input
    difficulty = input("Enter Easy, Medium, or Hard: ")
    while difficulty not in ["Easy", "Medium", "Hard"]:
        print("Invalid input. Please enter Easy, Medium, or Hard.")
        difficulty = input("Enter Easy, Medium, or Hard: ")

    # Set the maximum number based on the chosen difficulty
    if difficulty == "Easy":
        max_num = 100
    elif difficulty == "Medium":
        max_num = 500
    else:
        max_num = 1000

    num = random.randint(1, max_num) # Generates the random number

    attempts = 0 # Tracks the number of attempts
    correctGuess = False # loop condition for guessing

    # Main loop for guessing
    while not correctGuess:
        try:
            guess = int(input(f"Enter your guess (1-{max_num}): "))
            attempts += 1

            # Give feedback on guesses
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
    
    # Ask the user if they want to replay
    play_again = input("Do you want to play again? (Yes/No): ")
    while play_again.lower() not in ["yes", "No"]:
        play_again = input("Invalid input. Please enter Yes or No: ")
