#!/usr/bin/env python
# coding: utf-8


# def fibonacci(n):
#     if n < 2:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

memo = {0: 0, 1: 1}


def fibonacci(n):
    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]


def main():
    try:
        n = int(raw_input('Entre com um número inteiro: '))
        print 'fibonacci(%i) = %i' % (n, fibonacci(n))
    except ValueError:
        print 'Somente números inteiros são aceitos!'
        main()

if __name__ == '__main__':
    main()
