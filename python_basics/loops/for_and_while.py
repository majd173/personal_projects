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

def example(list_1):
    i = 0
    while i < 5:
        for x in list_1:
            if x == len(list_1):
                i += 1
    print(x)


example([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

