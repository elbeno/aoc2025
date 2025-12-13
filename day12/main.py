#!/usr/bin/env python3

import operator
import re
from functools import reduce


def read_input(filename):
    def convert(s):
        head, *tail = s.split()
        area = reduce(operator.mul, map(int, head[:-1].split('x')), 1)
        return [area] + list(map(int, tail))

    input = []
    with open(filename, "r") as f:
        for line in f:
            if re.match(r"^\d+x\d+:.*", line):
                input.append(convert(line))
    return input


def star1(input):
    regions = [1 for r in input if r[0] >= 9 * sum(r[1:])]
    return sum(regions)


def main():
    input = read_input("input")
    print(f"star1: {star1(input)}")


if __name__ == "__main__":
    main()
