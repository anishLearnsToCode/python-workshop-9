"""
list
index ---> value
unique     not unique
int        anything


:key        -->  value
unique      --> not unique
anything    --> anything

dictionary / hashmap / hashtable / map
- mutable
- iterable
"""

words = {
    'i': 520,
    'am': 100,
    'batman': 20,
    'hello': 100
}

# adding entries in dict
words['world'] = 23

# modify an entry
words['batman'] = 30

# key present in dict
print('ball' in words)

# access values
# print(words['ball'])

print(words.get('ball', 'hello'))

# remove values
del words['hello']

print(words)
