#!/usr/bin/python3

age = int(input("What is your age? - "))
gold_coins = int(input("How many gold coins do you have? - "))

if age >= 18 and gold_coins >= 20:
    print("You can enter")
else:
    print("You cannot enter")
