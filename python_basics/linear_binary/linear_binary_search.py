# linear search
def linear_search(target, array):
    for i in range(len(array)):
        if array[i] == target:
            print(f'Found {target} at index {i}')
            break
    else:
        print(f'{target} not found')


linear_search(5, [1, 2, 3, 4, 5])

# binary search
def binary_search(target, array):
    left = 0
    right = len(array) - 1
    for i in range(len(array)):
        mid = (left + right) // 2
        if array[mid] == target:
            print(f'Target found at index {mid}')
            break
        else:
            if mid < target:
                left = mid + 1
            else:
                right = mid - 1
    else:
        print(f'Target not found')


binary_search(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
