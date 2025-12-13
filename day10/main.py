#!/usr/bin/env python3

from functools import cache


def read_input(filename):
    input = []

    def convert(buttons, n):
        l = [int(x) for x in buttons[1:-1].split(",")]
        return sum(1<<c if c in l else 0 for c in range(n))

    with open(filename, "r") as f:
        for line in f:
            pattern, *rest = line.split()
            pat = sum(1<<c if pattern[c+1] == "#" else 0 for c in range(0, len(pattern)-2))
            input.append([pat, tuple(convert(x, len(pattern)-2) for x in rest[:-1])])

    return input


@cache
def num_presses(pattern, buttons):
    if pattern in buttons:
        return 1
    r = len(buttons)
    for n in range(r):
        b = buttons[n]
        new_buttons = buttons[:n] + buttons[n+1:]        
        r = min(r, num_presses(pattern ^ b, new_buttons))
    return 1 + r
    

def star1(input):
    return sum(num_presses(pat, buttons) for pat, buttons in input)


def main():
    input = read_input("input")
    print(f"star1: {star1(input)}")


if __name__ == "__main__":
    main()
