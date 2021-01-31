"""
{ x^2 | x in (0, 10)}
{ x + 2 | x in (5, 10) }
"""

g = [f'{x}' for x in range(1, 11)]
print(type(g))
print(g)


numbers = [x ** 2 for x in range(-10, 11)]
print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# n = int(input())
# print(sum(x for x in range(1, n + 1)))

print(sum([1, 2, 100, -90]))
