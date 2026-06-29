#!/usr/bin/python3

birth_year = int(input("What is your birth year? - "))

def calc_age(birth_year):
    age = 2026 - birth_year

    return age

print(f"If you were born in {birth_year} you're approximately {calc_age(birth_year)} years old")
