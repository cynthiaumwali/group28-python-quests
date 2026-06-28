secret_code = 42

attempts_used = 0
max_attempts = 3

while attempts_used < max_attempts:
    player_guess = input("What is your guess? ")
    player_guess = int (player_guess)

    if player_guess == secret_code:
        print("Wow! You cracked the code, well done!")
        break 

    else:
        attempts_used = attempts_used + 1 
        attempts_left = max_attempts - attempts_used
        if attempts_left > 0:
            print("Wrong code! You've got", attempts_left, "tries left")
        else:
            print("Sorry, you're out of tries! Better luck next time!")

