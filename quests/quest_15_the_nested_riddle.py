#!/usr/bin/python3
usr_input = input("DO you want to go left or right?: ")
if usr_input == "left":
    usr_choice = input("Do you want to swim or wait?: ")
    if usr_choice == "swim":
        print("Treasure found!")
    else:
        print("Try again later")
else:
    print("Try again later")
