#!/usr/bin/python3
def FizzBuzz_Test():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(i, "FizzBuzz")
            continue
        elif i % 3 == 0:
            print(i, "Fizz")
            continue
        elif i % 5 == 0:
            print(i, "Buzz")
            continue
        else:
            print(i)

FizzBuzz_Test()
