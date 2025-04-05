"""
Binary Search Algorithm: Implement a binary search function that efficiently finds an element in a sorted list.
"""

def search(sorted_list, item):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_list[mid] == item:
            return mid
        elif sorted_list[mid] < item:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(search([1,2,3,4], 3))
