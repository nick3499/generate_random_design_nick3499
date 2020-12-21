#!/usr/bin/env python
'''Generate random colored background design.'''
from random import randrange


def generate_design():
    '''Generate random background design.'''
    gradients = []
    n = 16
    for i in range(0, 36):
        gradients.append((n, n+6))
        n += 6

    gradients.append((232, 256))
    gradients_range = gradients[randrange(0, 37)]
    colors = []

    for i in range(0, 160):
        colors.append(f'\x1b[48;5;{randrange(gradients_range[0], gradients_range[1])}m \x1b[0m')

    join_cols = ''.join(colors)

    for i in range(0, 40):
        print(join_cols)


if __name__ == '__main__':
    generate_design()
