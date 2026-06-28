def adventure_begins():
    print("Welcome! Please choose your adventure: [1: Mountain Climbing, 2: Kayaking, 3: Paragliding]")
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
    print("You have chosen Mountain Climbing! Have fun!")
    exit_choice = input("Do you want to exit the adventure? (yes/no): ")
    if exit_choice.lower() == "yes":
        print("Goodbye! Thanks for playing!")
    else:
        adventure_begins()

def kayaking():
    print("You have chosen Kayaking! Enjoy the water!")
    exit_choice = input("Do you want to exit the adventure? (yes/no): ")
    if exit_choice.lower() == "yes":
        print("Goodbye! Thanks for playing!")
    else:
        adventure_begins()

def paragliding():
    print("You have chosen Paragliding! Enjoy the sky views!")
    exit_choice = input("Do you want to exit the adventure? (yes/no): ")
    if exit_choice.lower() == "yes":
        print("Goodbye! Thanks for playing!")
    else:
        adventure_begins()

adventure_begins()