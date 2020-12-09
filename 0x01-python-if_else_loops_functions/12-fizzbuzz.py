#!/usr/bin/python3
def fizzbuzz():
    for c in range(1, 101):
        if c % 3 == 0:
            print("Fizz", end="")
        if c % 5 == 0:
            print("Buzz", end="")
        if c % 3 and c % 5:
            print("{:d}".format(c), end="")
        print(end=" ")
