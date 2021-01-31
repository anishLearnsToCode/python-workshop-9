"""
map(func, iterable)
item_1  --> func(item_1)
item_2  --> func(item_2)
item_3  --> func(item_3)
item_4  --> func(item_4)
"""

numbers = [2, 3, 4, -10, 0]


def square(x: int) -> int:
    return x ** 2


numbers = list(map(int, input().split()))
print(numbers)
