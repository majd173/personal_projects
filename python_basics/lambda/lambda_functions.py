from functools import reduce
# Lambda Functions
multiply_function = lambda x, y: x * y
print(multiply_function(5, 6))

numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = reduce(lambda x, y: x * y, numbers_2)
print(product)

# Filtering

numbers_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_3))
print(even_numbers)

squared_numbers = list(map(lambda x: x ** 2, numbers_3))
print(squared_numbers)

array = [5, 4, 3, 2, 1]
sorted_array = sorted(array)
print(sorted_array)

array_2 = [5, 4, 3, 2, 1]
even_numbers_array = list(filter(lambda x: x % 2 == 0, array_2))
print(even_numbers_array)

array_3 = [5, 4, 3, 2, 1]
multiplied_ten_array_3 = list(map(lambda x: x * 10, array_3))
print(multiplied_ten_array_3)
