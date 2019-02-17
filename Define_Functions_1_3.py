from operator import mul, add


def square(x):
    return mul(x, x)


def sum_squares(x, y):
    return add(square(x), square(y))


print(square(5))
print(sum_squares(6, 8))

f = max
print(f)
max = 3
print(max)
print(f)
result = f(1, 2, 3)
# max(3,4)