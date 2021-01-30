"""
N
N!
0! = 1! = 1
"""

n = int(input())

i = 1
result = 1

while i <= n:
    result = result * i
    i += 1

print(result)

"""
n = 0
1
"""
