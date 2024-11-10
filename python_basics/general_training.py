# This page includes python functions need to be improved.
import json


# Example No: 1

def calculate_average(numbers):
    """
    This function calculates the average of a list of numbers.
    :param numbers:
    :return: average
    """
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
def is_even(number):
    """
    This function checks if a number is even.
    :param number:
    :return: True if the number is even, False otherwise.
    """
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

# Example No: 6
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
    with open("info.json", 'w') as file:
        json.dump(info, file, indent=4)

    with open("info.json", 'r') as file:
        print(file.read())


data_type_dic("Hello World")


# -------------------------------------------------------------------------------

# Example No: 7

def max_4(a, b, c, d):
    """
    This function prints the maximum value of four numbers.
    :param a:
    :param b:
    :param c:
    :param d:
    :return: The maximum value of four numbers.
    """
    if a > b:
        if a > c:
            if a > d:
                print(a)
            else:
                print(d)
        else:
            if c > d:
                print(c)
            else:
                print(d)
    else:
        if b > c:
            if b > d:
                print(b)
            else:
                print(d)
        else:
            if c > d:
                print(c)
            else:
                print(d)


max_4(4, 2, 3, 1)


# -------------------------------------------------------------------------------

# Example No: 8

def max_3(a, b, c):
    """
    This function prints the maximum value of three numbers.
    :param a:
    :param b:
    :param c:
    :return: The maximum value of three numbers.
    """
    if a > b:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        if b > c:
            print(b)
        else:
            print(c)


max_3(4, 2, 3)


# -------------------------------------------------------------------------------

# Example No: 9

def is_prime(number):
    """
    This function checks if a number is prime.
    :param number:
    :return: True if the number is prime, False otherwise.
    """
    if number % 2 == 0:
        print(False)
    else:
        print(True)


is_prime(4)


# -------------------------------------------------------------------------------

# Example No: 10

def primes_up_to(number):
    prime_numbers = [x for x in range(1, number) if x % 2 != 0]
    print(prime_numbers)


primes_up_to(20)


# -------------------------------------------------------------------------------

# Example No: 11

# def word_frequency(text):
#     text = text.split()
#     frequency = {}
#     first_word = text[0]
#     for word in text:
#         if text[word] != first_word:
#             frequency = {word: 1}
#         else:
#             frequency = {word: frequency[word] + 1}
#     print(frequency)
#
#
# word_frequency("hello hi hello")


# -------------------------------------------------------------------------------
#
# Example No: 12

def sum_of_unique_numbers(numbers):
    """
    This function returns the sum of unique numbers in a list.
    :param numbers:
    :return: sum of unique numbers
    """
    if len(numbers) >= 2:
        first = numbers[0]
        for number in numbers:
            if first == number:
                numbers.remove(number)
                numbers.remove(first)
                first = numbers[0]
            else:
                if first != number:
                    first = number
    print(sum(numbers))


sum_of_unique_numbers([1, 1, 2, 3, 3])


# -------------------------------------------------------------------------------


# Example No: 13

def fuzz_buzz():
    """
    This function prints Fuzz if the number is divisible by 3,
    FuzzBuzz if the number is divisible by 5,
    and FuzzBuzz if the number is divisible by both 3 and 5.
    """
    for i in range(1, 101):
        if i % 3 == 0:
            print("Fuzz")
        if i % 5 == 0:
            print("Buzz")
        if i % 3 == 0 and i % 5 == 0:
            print("FuzzBuzz")
        else:
            print(i)


fuzz_buzz()


# -------------------------------------------------------------------------------


# Example No: 14

def missing_number(numbers):
    first = numbers[0]
    if len(numbers) > 2:
        for number in numbers:
            if numbers[number] - numbers[number - 1] != 1:
                print(numbers[number] - 1)
                break


missing_number([1, 2, 4, 5, 6, 7])


# -------------------------------------------------------------------------------


# Example No: 15

def cypher_text(text, key):
    """
    This function encrypts a text with a given key.
    :param text:
    :param key:
    :return: cyphered text
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_text = []
    if len(text) > 1:
        for i in range(len(text)):
            if text[i] in alphabet:
                new_char = alphabet[(alphabet.index(text[i]) + key) % 26]
                new_text.append(new_char)
            else:
                new_text.append(text[i])
    new_text = "".join(new_text)
    print(new_text)


cypher_text("hello", 3)


# -------------------------------------------------------------------------------

# Example No: 16

def max_without_built_in(numbers):
    """
    This function returns the maximum number in a list.
    :param numbers:
    :return: maximum number
    """
    if len(numbers) > 1:
        first = numbers[0]
        for i in numbers:
            if i > first:
                first = i

    print(first)


max_without_built_in([1, 2, 4, 3, 5])


# -------------------------------------------------------------------------------

# Example No: 17

def is_anagram(word1, word2):
    """
    This function checks if two words are anagrams.
    :param word1:
    :param word2:
    :return: True if the words are anagrams, False otherwise.
    """
    word1_lower = word1.lower()
    word2_lower = word2.lower()
    count = 0
    for i in word1_lower:
        if i in word2_lower:
            count += 1

    if count == len(word1_lower):
        print(True)
    else:
        print(False)


is_anagram("hello", "llohe")
