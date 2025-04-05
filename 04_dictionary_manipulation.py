"""
Dictionary Manipulation: Create a program that counts the frequency of words in a given text and stores the results in a dictionary.
"""

# 1st attempt, misunderstood we need to count frequency of characters
# def count_frequency(string):
#     texts_dictionary = {}

#     for i in string:
#         if i == ' ':
#             continue
#         if i in texts_dictionary:
#             texts_dictionary[i] += 1
#         else:
#             texts_dictionary[i] = 1
#     return texts_dictionary


def count_frequency(string):
    texts_dictionary = {}

    for i in string.split(" "):
        if i in texts_dictionary:
            texts_dictionary[i] += 1
        else:
            texts_dictionary[i] = 1

    return texts_dictionary

print(count_frequency("Create a program that counts the frequence of words in a given text and stores the results in a dictionary"))

