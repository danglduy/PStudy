"""
Palindrome Checker: Create a function that checks if a string is a palindrome (reads the same backward as forward).
"""

def check_palindrome(string):

    # reversed will return an Iterator
    # return string == ''.join(reversed(string))

    # using slicing syntax. Negative number at the end indicates we will go backward
    # return string == string[::-1]

    # two pointers

    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
            continue

        return False

    return True

print(check_palindrome("assa"))


