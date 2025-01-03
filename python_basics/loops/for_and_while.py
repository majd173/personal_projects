# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in nums:
#     if num == 3:
#         break
#     print(num)
#
# nums_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in nums_2:
#     if num == 3:
#         continue
#     print(num)
#
# x = 3
# while x < 5:
#     print(x)
#     x += 1
#
# print([i for i in range(10) if i % 2 == 0])
#
#
# def nested():
#     for i in range(5):
#         for j in range(5):
#             print(f'{i}, {j}')
#
#
# nested()
#
#
# def remove_duplicated(list):
#     for num in list:
#         if list.count(num) > 1:
#             list.remove(num)
#     print(list)
#
#
# remove_duplicated([1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10])


# -----------------------------------------------------------------------------

# While loop example

# def example(list_1):
#     i = 0
#     while i < 5:
#         for x in list_1:
#             if x == len(list_1):
#                 i += 1
#     print(x)


# example([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# -----------------------------------------------------------------------------

# def while_example(a, b):
#     x = 0
#     while x < 5:
#         a = a + 1
#         b = b + 1
#         x += 1
#         print (f'{a},{b}')

# while_example(1, 2)


# -----------------------------------------------------------------------------
# This function removes duplicate numbers from a list and sorts the list.

def remove_duplicates_example(lst):
    for i in lst:
        if lst.count(i) > 1:
            lst.remove(i)
    return sorted(lst)


print(remove_duplicates_example([1, 2, 2, 55, 55, 3, 3, 3, 44, 5, 6, 44]))

# -----------------------------------------------------------------------------
