#!/usr/bin/python3

def adventure_begins():
    print("Welcome! Choose your adventure: [1: Mountain Climbing, 2: Kayaking, 3: Paragliding]")
    user_choice = input("Enter the number of your choice: ")
    if user_choice == "1":
        mountain_climbing()
    elif user_choice == "2":
        kayaking()
    elif user_choice == "3":
        paragliding()
    else:
        print("Invalid choice. Please choose a correct number.\n")
        adventure_begins()

def mountain_climbing():
    print("\nYou have chosen Mountain Climbing!\nYou are halfway up. The cold is getting too much.")
    choice = input("Do you [1: keep climbing, 2: go back down]? ")
    if choice == "1":
        print("\nCongratulations! You have reached the top of the mountain.")
    elif choice == "2":
        print("\nYou headed back down safely.")
    else:
        print("Invalid choice.")
        mountain_climbing()

def kayaking():
    print("\nYou have chosen Kayaking!\nYou are on the river. A storm is approaching.")
    choice = input("Do you [1: keep paddling, 2: go back to the shore]? ")
    if choice == "1":
        print("\nCongratulations! You made it through the storm.")
    elif choice == "2":
        print("\nYou are back to the shore.")
    else:
        print("Invalid choice.")
        kayaking()

def paragliding():
    print("\nYou have chosen Paragliding!\nYou are up in the air. The wind is getting stronger.")
    choice = input("Do you [1: stay up, 2: go back down]? ")
    if choice == "1":
        print("\nCongratulations! You completed the flight.")
    elif choice == "2":
        print("\nYou are back on the ground.")
    else:
        print("Invalid choice.")
        paragliding()

adventure_begins()