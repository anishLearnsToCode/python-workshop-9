# break
# for i in range(10):
#     if i == 4:
#         print(i)
#     break


# for i in range(5):
#
#     for j in range(3):
#         if i + j == 2:
#             break
#         print(i + j, end=' ')
#
#     print()

# continue
# for i in range(10):
#     print(i)
#     continue

for i in range(1, 6):

    for j in range(i + 1):
        if j % i == 0:
            continue
        print(i + j, end=' ')
        if j % 3 == 0:
            break

    print()

"""
i = 5
j = 3

3 
4 5
5 6 7
6 7 8

"""
