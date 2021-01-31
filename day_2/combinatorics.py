def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def permutation(n: int, r: int) -> int:
    """:returns nPr = n! / (n - r)!"""
    return factorial(n) // factorial(n - r)

    # n = 4, r = 1
    # return factorianl(4) / factorial(4 - 1)
    # return factorianl(4) / factorial(3)
    # return 24 / factorial(3)
    # return 24 / 6
    # return 4


def combination(n: int, r: int) -> int:
    """:returns nCr = nPr / r!"""
    return permutation(n, r) // factorial(r)


print(combination(5, 0))
print(combination(5, 1))
print(combination(5, 2))
print(combination(5, 3))
print(combination(5, 4))
print(combination(5, 5))
