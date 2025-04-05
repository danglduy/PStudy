"""
Generator Function: Write a generator function that yields the Fibonacci sequence up to a specified number.
"""

def fizbo_till(max_num):
    sequence = [0, 1]
    end = len(sequence) - 1

    while sequence[end] < max_num:
        sequence.append(sequence[end] + sequence[end - 1])
        end = len(sequence) - 1
        yield sequence

a = fizbo_till(2000)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


# [0, 1, 1]
# [0, 1, 1, 2, 3]
# [0, 1, 1, 2, 3, 5]
# [0, 1, 1, 2, 3, 5, 8]
# [0, 1, 1, 2, 3, 5, 8, 13]
# [0, 1, 1, 2, 3, 5, 8, 13, 21]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
