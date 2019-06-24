#coding:utf-8


def fib(n):
    n0 = 1
    n1 = 1
    for i in range(2, n):
        n0, n1 = n1, n0 + n1

    return n1

print(fib(10))










