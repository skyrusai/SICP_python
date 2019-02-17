from operator import mul


def square(x):
    return mul(x, x)


def print_square(x):
    return print(square(x))


def absolute_result(x):
    if x > 0:
        return x
    elif x < 0:
        return -x
    else:
        return 0


print(absolute_result(0))
print(absolute_result(2))
print(absolute_result(-2))


def fib(n):
    """commpute the nth Fibonacci number ,for n>=2"""
    if n == 1:
        return 0
    a, b = 0, 1
    k = 2
    while k < n:
        a, b = b, a + b
        k += 1
    return b


print(fib(1))
print(fib(2))
print(fib(3))


def fib_test():
    assert fib(2) == 1, "8th Fibonacci number should be 13"
    assert fib(1) == 0, "8th Fibonacci number should be 13"
    assert fib(3) == 1, "8th Fibonacci number should be 13"
    assert fib(8) == 13, "8th Fibonacci number should be 13"
    assert fib(8) == 13, "8th Fibonacci number should be 3"


# fib_test()

def sum_naturals(n):
    """sum of naturals 1-n.

    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


from doctest import run_docstring_examples
from doctest import testmod

run_docstring_examples(sum_naturals, globals(), True)
testmod()
# python -m doctest control_1_5.py
