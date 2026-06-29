# Quest 24: The Master Spell
# Concept: Calling a function from within another, by passing one function's
# return value into another function as an argument.

def ask_for_age():
    #Asks the user for their age and returns it as an integer.
    age = int(input("How many years have you walked this realm? "))
    return age

def can_they_vote(age):
    #Takes an age and prints whether that age qualifies for voting.
    if age >= 18:
        print("You are old enough to vote in the kingdom's elections.")
    else:
        print("You must wait a few more years before you may vote.")

# First, call ask_for_age() to get the user's age
players_age = ask_for_age()

# Then pass that result into can_they_vote() to make the decision
can_they_vote(players_age)