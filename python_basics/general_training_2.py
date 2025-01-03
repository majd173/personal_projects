# # Example No: 1
import datetime


def capitalize_first_letter(string):
    print(string.title())


capitalize_first_letter("hello world")


# -------------------------------------------------------------------------------
# Example No: 2

def second_large(list):
    list.remove(max(list))
    return max(list)


list = [17, 5, 66, 99]

print(second_large(list))


# -------------------------------------------------------------------------------

# Example No: 3

def capitalize_each_word(string):
    return " ".join(word.capitalize() for word in string.split(" "))


print(capitalize_each_word("hello world"))


# -------------------------------------------------------------------------------


def convert_to_decimal(num):
    x = 0
    listed_number = reversed([int(i) for i in str(num)])
    new_list = []
    for i in listed_number:
        new_list.append(2 ** x if i == 1 else 0)
        x += 1
    print(sum(new_list))


number = 10011001
convert_to_decimal(number)


# -------------------------------------------------------------------------------

def reverse_and_uppercase(string):
    return string[::-1].upper()


print(reverse_and_uppercase("hello world"))


# -------------------------------------------------------------------------------

# Example No: 4

def even_number(list):
    return [i for i in list if i % 2 == 0]


print(even_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# -------------------------------------------------------------------------------

# Example No: 5
def count_occurrences(string):
    dict = {}
    for i in string:
        count = string.count(i)
        dict[i] = count
    return dict


print(count_occurrences("hello world"))


# -------------------------------------------------------------------------------

# Example No: 6

def common_elements(list_1, list_2):
    new_set = set()
    for i in list_1:
        if i in list_2:
            new_set.add(i)
    return new_set


print(common_elements([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))


# -------------------------------------------------------------------------------

# Example No: 7

def convert_to_float(list):
    new_list = []
    return [float(i) for i in list if i is not None and type(i) == float or type(i) == int]


print(convert_to_float([1, 2, 3, 4, 5.5, 6, 7, "aaa", 9, 10]))


# -------------------------------------------------------------------------------

# Example No: 8

def check_all_positive(list):
    check = False
    for i in list:
        if i % 2 == 0:
            check = True
        else:
            check = False
        return check


print(check_all_positive([2, 4, 6, 8, 10]))


# -------------------------------------------------------------------------------