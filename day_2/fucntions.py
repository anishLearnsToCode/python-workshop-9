"""
def function_name(parameter_1, parameter_2, parameter_3 ...):
    code
    code
    return value_1, value_2 ....
"""


def hello():
    print('hello world')


def hello_world(name):
    print(f'hello {name}')


def addition(a, b):
    return a + b


def full_name(first_name: str, last_name: str, middle_name=None) -> str:
    if middle_name is None:
        return first_name + ' ' + last_name
    return first_name + ' ' + middle_name + ' ' + last_name


print(full_name('alan', 'turing'))
print(full_name('wolfgang', 'mozart', 'amadeus'))
print(full_name('lady', 'lovelace', 'ada countess of'))
print(full_name(last_name='einstien', first_name='albert'))
print(full_name('johannass', middle_name='sebastian', last_name='bach'))
