# list = [1, 2, 3, 4, 5]
# list.pop(2)
# print(list)
# --------------------------------------------------------------------------------
# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, value):
#         self.stack.append(value)
#
#     def pop(self):
#         return self.stack.pop()
#
#     def peek(self):
#         return self.stack[-1]
#
#
# example = Stack()
# example.push(5)
# print(example.stack)
# --------------------------------------------------------------------------------
# map = {
#     1: 'value1',
#     2: 'value2'}
#
# map[3] = 'value3'
# map[2] = "new_value2"
# print(map)
# --------------------------------------------------------------------------------
# array = [1, 2, 3, 4, 5]
# print(array[2:4])
# --------------------------------------------------------------------------------
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[-1]
#     left = []
#     for x in arr[:-1]:
#         if x < pivot:
#             left.append(x)
#     right = []
#     for x in arr[:-1]:
#         if x >= pivot:
#             right.append(x)
#     return quick_sort(left) + [pivot] + quick_sort(right)
#
#
# array = [5, 4, 3, 2, 1]

# print(quick_sort(array))
# --------------------------------------------------------------------------------
# def linear_search(arr, tar):
#     for x in range(len(arr)):
#         if arr[x] == tar:
#             return x
#         elif x == len(arr) - 1:
#             return "Not Found"
#
#     return "Not Found"
#
#
# array = [5, 4, 3, 2, 1]
# target = 3
# print(linear_search(array, target))
# --------------------------------------------------------------------------------
# def binary_search(arr, tar):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == tar:
#             return mid
#         elif arr[mid] < tar:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return "Not Found"
#
#
# array = [5, 4, 3, 2, 1]
# target = 7
# print(binary_search(array, target))
