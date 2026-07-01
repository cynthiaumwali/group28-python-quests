#!/usr/bin/env python3
import random

guess = int(input("Enter a number, take a lucky guess: "))
secret_number = random.randint(0,10)

while guess != secret_number: 
    if guess > secret_number:
        print("It's too high")
    elif guess < secret_number:
        print("It's too low")

    guess = int(input("Enter a number, take a lucky guess: "))
else:
    print ("Good Job ! You got it right: ", secret_number)
