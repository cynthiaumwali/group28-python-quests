#!/usr/bin/python3

password = "Test@123"
user_input = input("Welcome!\nPassword: ")

def check_pswd(input):
    if (input == password):
        print("Access Granted")
    else:
        print("Access Denied")

check_pswd(user_input)
