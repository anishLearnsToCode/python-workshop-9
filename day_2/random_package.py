import random

a, b = -100, 100
# r = int((b - a) * random.random() + a)
print(random.randint(a, b))
# print(r)

"""
r in (0, 1)
(0, 1) * 10
(0, 10)

(0, 1) * 8 + 2
(0, 8) + 2
(2, 10)

(0, 1) * (b - a) + a
(0, b - a) + a
(a, b)
"""
