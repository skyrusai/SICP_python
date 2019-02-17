def sum_(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def cubes(k):
    return k * k * k


def sum_cubes(n):
    return sum_(n, cubes)


print(sum_cubes(5))


def naturals(k):
    return k


def sum_natuals(n):
    return sum_(n, naturals)


print(sum_natuals(5))
