#!/usr/bin/env python
# coding: utf-8


# def fibonacci(number):
#     if number < 2:
#         return number
#     else:
#         return fibonacci(number - 1) + fibonacci(number - 2)

memo = {0: 0, 1: 1}


def fibonacci(number):
    if number not in memo:
        memo[number] = fibonacci(number - 1) + fibonacci(number - 2)
    return memo[number]


def main():
    try:
        number = int(raw_input('Entre com um número inteiro: '))
        print 'fibonacci(%i) = %i' % (number, fibonacci(number))
    except ValueError:
        print 'Somente números inteiros são aceitos!'
        main()

if __name__ == '__main__':
    main()
