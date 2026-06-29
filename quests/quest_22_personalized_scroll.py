#!/usr/bin/python3

def personalized_greeting(name, quest):
    return f"Hi {name}! Welcome to the {quest} quest!"

name = input("Enter your name: ")
quest = input("Enter the quest name: ")
print(personalized_greeting(name, quest))