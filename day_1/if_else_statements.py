"""
if condition_1:
    code
    code
elif condition_2:
    code
elif condition_3:
    code
..
..
..
else:
    code


elif not compulsory
else not compulsory
"""

number = int(input())

if number == 0:
    print('i am in the if block')
    print('i am leaving')
elif number < 10:
    print('small number')
elif number < 100:
    print('mehhhh')
elif number < 20:
    print('okayish number')

print('i am outside if else')
