# Quest 18: The Loop of Riddles
# Concept: while loop that keeps running until the user provides correct input

secret_number = 7
guess = None  # Start with no guess yet, so the loop is guaranteed to run at least once

# Keep looping as long as the guess does not match the secret number
while guess != secret_number:
    guess = int(input("Guess the secret number (1-10): "))

    if guess != secret_number:
        print("Wrong! Try again.")

print("You guessed it! The secret number was", secret_number)