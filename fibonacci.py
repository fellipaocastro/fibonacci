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
