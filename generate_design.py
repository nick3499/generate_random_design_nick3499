#!/usr/bin/env python
'''Generate random colored background design.'''
from random import randrange

def generate_design():
    '''Generate random background design.'''
    # input instructions
    print('\x1b[1;34mEnter hex color\x1b[0m: (example: 50514f) or leave blank')

    # hex color code string inputs
    hex1 = input('hex 1: ').upper() or '000000'
    hex2 = input('hex 2: ').upper() or '000000'
    hex3 = input('hex 3: ').upper() or '000000'
    hex4 = input('hex 4: ').upper() or '000000'
    hex5 = input('hex 5: ').upper() or '000000'

    # concatenated hex strings
    hex_strs = hex1 + hex2 + hex3 + hex4 + hex5

    # hex pairs
    hex_pairs = []
    n = 0
    for i in range(0, 5):
        hex_pairs.append([hex_strs[n:n+2], hex_strs[n+2:n+4], hex_strs[n+4:n+6]])
        n += 6

    # convert hex pairs to ASCII numbers
    ascii_nums = []
    for i in range(0, 5):
        ascii_nums.append([int(hex_pairs[i][0], 16), int(hex_pairs[i][1], 16),
            int(hex_pairs[i][2], 16)])

    # generate random, color-schemed background
    colors = []  # color scheme strings
    for i in range(0, 5):
        colors.append(f'\x1b[48;2;{ascii_nums[i][0]};{ascii_nums[i][1]};\
{ascii_nums[i][2]}m \x1b[0m')

    color_strings = ''
    for i in range(0, 160):
        color_strings += colors[randrange(0, 5)]

    for i in range(0, 40):
        print(color_strings)


if __name__ == '__main__':
    generate_design()
