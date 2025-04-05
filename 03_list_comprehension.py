"""
List Comprehension Practice: Write a function that takes a list of numbers and returns a new list containing only the even numbers.
"""

def list_even(numbers):
    return [i for i in numbers if i % 2 == 0]

print(list_even(range(10)))
