"""
1 2 3 4 -100 4    5 6
[1, 2, 3, 4, -100, 4, 5, 6]
"""

user_input = input()
numbers = user_input.split()
print(numbers)

for index in range(len(numbers)):
    numbers[index] = int(numbers[index])
    print(numbers)
