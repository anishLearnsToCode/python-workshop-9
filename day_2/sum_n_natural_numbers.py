def sum_n_natural_numbers(n: int) -> int:
    """:returns 1 + 2 + 3 + 4 + ... + n"""
    result = 0
    for i in range(n + 1):
        result = result + i
    return result


# print(sum_n_natural_numbers(0))
# print(sum_n_natural_numbers(1))
# print(sum_n_natural_numbers(2))
# print(sum_n_natural_numbers(3))
# print(sum_n_natural_numbers(4))
# print(sum_n_natural_numbers(5))
# print(sum_n_natural_numbers(6))

n = int(input())
print(sum_n_natural_numbers(n))
