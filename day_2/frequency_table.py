"""
passage
i am very tired, but this is very good class i am learning many new things dictionary is amazing
this is very interesting i like this this is new
{
    'i': 3,
    'am': 4,
    'very': 2,
    'hello': 2,
    'ball': 1
}
"""

passage = input()
words = passage.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1


print(freq)

"""
passage = hello world
words = ['hello', 'world']
freq = {}
word = 'hello'
freq['hello'] += 1
freq['hello'] = freq.get('hello', 0) + 1
"""
