#!/usr/bin/env python
'''Generate random colored background.
ref. https://coolors.co/020202-0d2818-04471c-058c42-16db65'''
from random import randrange

def generate_design():
    '''Generate random background design.'''
    # input hex color codes
    print('\x1b[1;34mEnter hex color\x1b[0m: (example: 50514f) or leave blank')

    hex1 = input('hex 1: ').upper()  # hex color code inputs
    hex2 = input('hex 2: ').upper()
    hex3 = input('hex 3: ').upper()
    hex4 = input('hex 4: ').upper()
    hex5 = input('hex 5: ').upper()

    # split hex color code into hex pairs
    hex_pairs = {
        'p1': [hex1[:2], hex1[2:4], hex1[4:]],
        'p2': [hex2[:2], hex2[2:4], hex2[4:]],
        'p3': [hex3[:2], hex3[2:4], hex3[4:]],
        'p4': [hex4[:2], hex4[2:4], hex4[4:]],
        'p5': [hex5[:2], hex5[2:4], hex5[4:]]}
    ascii_nums = []

    # convert hex pairs to ASCII
    for i in hex_pairs:
        try:
            ascii_list = [
                int(hex_pairs[i][0], 16),
                int(hex_pairs[i][1], 16),
                int(hex_pairs[i][2], 16)]
            ascii_nums.append(ascii_list)
        except ValueError:
            ascii_nums.append([0, 0, 0])

    # generate color-schemed background
    color_strings = ''
    colors = [
        f'\x1b[48;2;{ascii_nums[0][0]};{ascii_nums[0][1]};\
{ascii_nums[0][2]}m \x1b[0m',
        f'\x1b[48;2;{ascii_nums[1][0]};{ascii_nums[1][1]};\
{ascii_nums[1][2]}m \x1b[0m',
        f'\x1b[48;2;{ascii_nums[2][0]};{ascii_nums[2][1]};\
{ascii_nums[2][2]}m \x1b[0m',
        f'\x1b[48;2;{ascii_nums[3][0]};{ascii_nums[3][1]};\
{ascii_nums[3][2]}m \x1b[0m',
        f'\x1b[48;2;{ascii_nums[4][0]};{ascii_nums[4][1]};\
{ascii_nums[4][2]}m \x1b[0m']

    for i in range(0, 160):
        color_strings += colors[randrange(0, 5)]

    for i in range(0, 40):
        print(color_strings)


if __name__ == '__main__':
    generate_design()
