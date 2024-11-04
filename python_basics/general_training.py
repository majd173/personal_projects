# This page includes python functions need to be improved.
import json


# Example No: 1
# Prints the average of a list of numbers
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average


# Improved version
def calculate_average_improved(numbers):
    if len(numbers) == 0:
        return 0
    print(sum(numbers) / len(numbers))


calculate_average_improved([1, 2, 3, 4, 5])


# -------------------------------------------------------------------------------


# Example No: 2
# Checks if a number is even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# Improved version
def is_even_improved(number):
    print(number % 2 == 0)


is_even_improved(5)


# -------------------------------------------------------------------------------

# Example No: 3
# Capitalize each word in a list
def capitalize_words(words):
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    return capitalized_words


# Improved version
def capitalize_words_improved(words):
    print([word.capitalize() for word in words])


capitalize_words_improved(["hello", "world"])


# -------------------------------------------------------------------------------

# Example No: 4
# Checks if a word is a palindrome

def is_palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False


# Improved version
def is_palindrome_improved(word):
    print(word.lower() == word[::-1])


is_palindrome_improved("racecar")


# -------------------------------------------------------------------------------

# Example No: 5
# Counts the number of vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


# Improved version
def count_vowels_improved(text):
    print(count_vowels(char for char in text if char in "aeiouAEIOU"))


count_vowels_improved("hello")


# -------------------------------------------------------------------------------
def data_type_dic(value):
    """
    This function prints the data-type of a value and its properties in a text file.
    :param value:
    """
    info = {
        "Data Type": str(type(value)),
        "Is_numeric": isinstance(value, (int, float)),
        "Is_sequence": isinstance(value, (str, list, tuple, dict, set)),
        "Length": len(value) if isinstance(value, (str, list, tuple, dict, set)) else None
    }
    with open("info.txt", 'w') as file:
        json.dump(info, file, indent=4)

    with open("info.txt", 'r') as file:
        print(file.read())


data_type_dic("Hello World")
