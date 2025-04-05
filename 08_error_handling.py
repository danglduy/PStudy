"""
Error Handling: Create a function that divides two numbers but handles potential errors (like division by zero) with appropriate try/except blocks.
"""

def divide(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by 0")
    except Exception as e:
        print(f"There are some errors: {e}")

divide(10,0)
divide(10,2)

