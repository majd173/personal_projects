list = [1, 8, 3, 7, 9, 5, 2, 4, 6]


# list.clear()
#
# list_copy = list.copy()
#
# list_count = list.count(2)
#
# list.extend([10, 11, 12])
#
# list.insert(0, 15)
#
# list.remove(1)
#
# list.reverse()
#
# print(list)
#
# # Random
# import random
#
# random.shuffle(list)
# print(list)
#
# numbers = random.choice(list)
# print(numbers)
#
#
# def second_largest(list):
#     list.remove(max(list))
#     return max(list)
#
#
# print(second_largest(list))


def second_largest_improved(list_1):
    while len(list) > 2:
        first, second = list_1[0], 0
        for i in list_1:
            if i > first:
                first, second = i, first
            else:
                if second < i < first:
                    second = i
                    first = first

        print(second)
        return


second_largest_improved(list)
