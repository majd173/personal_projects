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

# Example No: 9

def example(string):
    list = []
    for i in string:
        if i.isalpha() == True or i.isspace() == True:
            continue
        else:
            list.append(i)

    return len(list)


print(example("hello11 world"))


# -------------------------------------------------------------------------------


# Example No: 10

def list_example(list):
    new_list = [i + x for i, x in enumerate(list)]
    return new_list


print(list_example([1, 2, 3, 4, 5]))


# -------------------------------------------------------------------------------


def list_example_2(list):
    for index, value in enumerate(list):
        print(f'"Index:" {value}, "Value:" {index}')


print(list_example_2([1, 2, 3, 4, 5]))


# -------------------------------------------------------------------------------

# Example No: 11

def set_example(list):
    my_set = set(list)
    my_set.add(6)
    my_set.pop()
    print(max(my_set))
    print(sorted(my_set))
    print(my_set.symmetric_difference({7, 8, 9}))
    print(my_set.union({7, 8, 9}))
    print(my_set.intersection({7, 8, 9}))
    print(my_set.difference({7, 8, 9}))

set_example([1, 2, 3, 4, 5, 8, 6, 7])


# -------------------------------------------------------------------------------


# Example No: 12

def tuple_example(list):
    my_tuple = tuple(list)
    print(max(my_tuple))
    print(my_tuple)
    print(sorted(my_tuple))



tuple_example([1, 2, 3, 4, 5, 9, 7])
