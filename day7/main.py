#!/usr/bin/env python3

import re
from functools import reduce


def read_input(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def scan(f, seq, init):
    yield init
    for value in seq:
        init = f(init, value)
        yield init


def advance(acc, l2):
    l1, splits = acc

    def combine(c1, c2):
        if c1 == "|":
            return c1 if c2 != "^" else "s"
        return c2

    s = "".join(map(combine, l1, l2))

    pat = r"(.)s(.)"
    rep = r"|^|"
    splits += len(re.findall("s", s))
    new_s = re.sub(pat, rep, s)
    while new_s != s:
        s = new_s
        new_s = re.sub(pat, rep, s)
    return s, splits


def star1(grid):
    _, splits = reduce(advance, grid[1:], (grid[0], 0))
    return splits


def advance2(beams, splitters):
    for i in range(len(beams)):
        if splitters[i] == '^':
            beams[i-1] += beams[i]
            beams[i+1] += beams[i]
            beams[i] = 0
    return beams


def star2(grid):
    beams = [1 if c == '|' else 0 for c in grid[0]]
    return sum(reduce(advance2, grid[1:], beams))


def main():
    grid = read_input("input")
    grid[0] = grid[0].replace("S", "|")
    print(f"star1: {star1(grid)}")
    print(f"star2: {star2(grid)}")


if __name__ == "__main__":
    main()
