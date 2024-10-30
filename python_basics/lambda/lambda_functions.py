from functools import reduce

multiply = lambda x, y: x * y
print(multiply(5, 6))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = list(map(lambda x: x**2, numbers))
print(squared)

numbers_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product = reduce(lambda x, y: x * y, numbers_2)
print(product)