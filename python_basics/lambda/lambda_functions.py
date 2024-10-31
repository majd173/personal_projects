from functools import reduce
#
multiply = lambda x, y: x * y
print(multiply(5, 6))


numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = reduce(lambda x, y: x * y, numbers_2)
print(product)

# Filtering

numbers_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x%2 == 0, numbers_3))
print(even_numbers)

squared_numbers = list(map(lambda x: x**2, numbers_3))
print(squared_numbers)