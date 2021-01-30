"""
while condition:
    code
    code

condition -> true -> code -> condition -> true -> code -> condition -> false -> exit loop
"""

# infinite loop
# while True:
#     print('hello')

i = 0
while i < 5:
    print(i)
    i += 2

print('i am outside the loop')
print(i)

"""
i = 6
0
2
4
i am outside loop
6
"""
