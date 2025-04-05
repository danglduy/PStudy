"""
Recursive Function: Create a recursive function to calculate the factorial of a number without using loops.
"""

def fractional(n):
    if n == 0 or n == 1:
        return n

    return n * fractional(n - 1)

print(fractional(5))
