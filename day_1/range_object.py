"""
Range Object

range(stop)
range(start, stop)
range(start, stop, step)

start = 0
step = 1
stop: user needs yo define

[start, stop)

- immutable (not modify once made)
- iterable (you an iterate on it)
- strings are also iterable
"""

r = range(5, 10, 2)

print(type(r))
print(r.start)
print(r.stop)
print(r.step)
