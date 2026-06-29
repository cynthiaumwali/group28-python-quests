# Quest 12: The Two-Path Cave
# Concept: if-else statement - provides an alternative path when the condition is false

correct_password = "openthecave"

entered_password = input("Enter the secret password: ")

# If the entered password matches, grant access.
# Otherwise (else), deny it - this covers every other possible input.
if entered_password == correct_password:
    print("Access Granted! The cave door creaks open.")
else:
    print("Access Denied. The cave remains sealed.")