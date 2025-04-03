"""
Palindrome Checker: Create a function that checks if a string is a palindrome (reads the same backward as forward).
"""

def check_palindrome(string):
    return string == ''.join(reversed(string))



print(check_palindrome("aaaaa"))


