# generate_random_design_nick3499
Generate random design which displays in terminal emulator

![screen capture](screen_capture.png)

## Unix Shebang

The human-readable Unix shebang `#!` translates to the magic number `0x23 0x21`. Based on the shebang line `#!/usr/bin/env python`, the `env` shell command interprets the `generate_design.py` text file as a Python app.

```python
>>> hex(ord('#'))
'0x23'
>>> hex(ord('!'))
'0x21'
```

## Documentation

```python
>>> __doc__
'Generate random colored background design.'
>>> generate_design.__doc__
'Generate random background design.'
```

- `__doc__` string contains module's documentation
- `generate_design.__doc__` string contains the function's documentation

## Import

```python
from random import randrange
```

The `random.randrange()` method is used to generate a random number from 1 to 5, in order to randomly select one color from the scheme.

## function

```python
def generate_design():
```

The block keyword `def` starts the definition and organization of the function's code; the `generate_design()` method's code block.

## Inputs

```python
print('\x1b[1;34mEnter hex color\x1b[0m: (example: 50514f) or leave blank')

hex1 = input('hex 1: ').upper() or '000000'
hex2 = input('hex 2: ').upper() or '000000'
hex3 = input('hex 3: ').upper() or '000000'
hex4 = input('hex 4: ').upper() or '000000'
hex5 = input('hex 5: ').upper() or '000000'
```

The `input()` builtin function returns a prompt for user input. The following is an example of such input:

```shell
Enter hex color: (example: 50514f) or leave blank
hex 1: 020202
hex 2: 0d2818
hex 3: 04471c
hex 4: 058c42
hex 5:
```

Since the `hex 5:` input was left blank, `hex5` will default to `'000000'`

# Concatenated Hex Strings

```python
hex_strs = hex1 + hex2 + hex3 + hex4 + hex5
```

Hex color code inputs are all concatenated into a single string.

```python
'0202020d281804471c058c42000000'
```

## Generate Hex Pair List

```python
hex_pairs = []
n = 0
for i in range(0, 5):
    hex_pairs.append([hex_strs[n:n+2], hex_strs[n+2:n+4], hex_strs[n+4:n+6]])
    n += 6
```

`n` is used to set the first index point in the long string for the start of each hex pair list. Slice notation is used to separate each 6-character code into three items. For example, the hex color code `'058c42'` splits to `['05', '8c', '42']`, which represents a specific color.

## Convert to ASCII

```python
ascii_nums = []
for i in range(0, 5):
    ascii_nums.append([int(hex_pairs[i][0], 16), int(hex_pairs[i][0], 16),
        int(hex_pairs[i][0], 16)])
```

Hex pairs are converted to ASCII code decimal numbers, as demonstrated below:

```python
>>> int('05', 16)
5
>>> int('8c', 16)
140
>>> int('42', 16)
66
```

The ASCII value numbers will used for color formatting: `f'\x1b[48;2;5;140;66m \x1b[0m'`.

- `\x1b[` sequence escapes the color formatting.
- `48;2;` sequence sets formatting to background color.
- `5;140;66m` sequence sets RGB color values.
- `\x1b[0m` sequence sets color to default.

## Generate Design

```python
colors = []  # color scheme strings
for i in range(0, 5):
    colors.append(f'\x1b[48;2;{ascii_nums[i][0]};{ascii_nums[i][1]};{ascii_nums[i][2]}m \x1b[0m')

color_strings = ''
for i in range(0, 160):
    color_strings += colors[randrange(0, 5)]

for i in range(0, 40):
    print(color_strings)
```

The f-string `f'\x1b[48;2;{ascii_nums[0][0]};{ascii_nums[0][1]};{ascii_nums[0][2]}m \x1b[0m'` background color formats a single space. The sequence `48;2;` is for background color modification, followed by `13;40;24`, which sets RGB values, for example.

The first `for` loop generates a list which is assigned to `colors` variable. A list of formatted background-colored spaces.

The second `for` loop interates the `color_pattern += colors[randrange(1, 5)]` instruction which appends a random background-color space to the `color_pattern` attribute. The `randrange(1, 5)` call returns an integer from 1 to 5 which is used to pick a random color index.

The third `for` loop simply repeats the generated random pattern stored in `color_pattern` to the extent of 40 identical lines.

## If Block

```python
if __name__ == '__main__':
    generate_design()
```

The final `if` block executes the `generate_design()` method of the script runs as a standalone app. For example, if this app was imported into another app, its `__name__` would no longer be `__main__`, so `generate_design()` would not execute unless it was called.
