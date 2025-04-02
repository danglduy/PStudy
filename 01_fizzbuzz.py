"""
FizzBuzz Challenge: Write a program that prints numbers from 1 to 100, but for multiples of 3 print "Fizz", for multiples of 5 print "Buzz", and for multiples of both print "FizzBuzz".
"""

start = 1
end = 100
numbers = range(start, end + 1)

for x in list(numbers):
    if x % 15 == 0:
        print(f"{x} - FizzBuzz")
    elif x % 3 == 0:
        print(f"{x} - Fizz")
    elif x % 5 == 0:
        print(f"{x} - Buzz")

