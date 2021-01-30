"""
N
1^2 + 2^2 + 3^2 + ... + N^2
"""

n = int(input())

i = 1
result = 0

while i <= n:
    result += i ** 2
    i += 1

print(result)

"""
n = 3
i = 2
result = 4
"""