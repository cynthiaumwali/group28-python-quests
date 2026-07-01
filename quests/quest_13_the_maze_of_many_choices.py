#!/usr/bin/env python3

num = int(input("Insert a grade between the range 0-100: "))

if num >= 90: 
    print("You've scored an A-grade")
elif 80 <= num  <= 89:
    print("You've scored a B-grade")
elif 70<= num <= 79:
    print("You've scored a C-grade")
else:
    print("There is a need for improvement")

