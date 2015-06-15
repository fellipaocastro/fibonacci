#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import

from fibonacci import fibonacci


def main():
    try:
        number = int(raw_input('Entre com um número inteiro: '))
        print 'fibonacci({}) = {}'.format(number, fibonacci(number))
    except ValueError:
        print 'Somente números inteiros são aceitos!'
        main()

if __name__ == '__main__':
    main()
