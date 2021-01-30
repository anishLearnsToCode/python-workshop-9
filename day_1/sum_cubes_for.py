"""
N
1^3 + 2^3 + 3^3 + ... + N^3
"""

n = int(input())
result = 0

for i in range(1, n + 1):
    result = result + i ** 3

print(result)
