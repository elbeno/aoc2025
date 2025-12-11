#!/usr/bin/env python3

import operator
from functools import reduce
from itertools import takewhile


def normalize(input):
    max_len = max(len(line) for line in input)
    return [f"{line:<{max_len}}" for line in input]


def read_input(filename):
    with open(filename, "r") as f:
        return normalize([line[:-1] for line in f])


ops = {"*": operator.mul, "+": operator.add}


def star1(input):
    def apply(row):
        head, *tail = row
        return reduce(ops[head], map(int, tail))

    split_lines = [line.split() for line in input]
    return reduce(operator.add, map(apply, zip(*split_lines)))


def chunks(lines):
    def pred(x):
        return not all(c == " " for c in x)

    chunk = list(takewhile(pred, lines))
    while len(chunk) != 0:
        yield chunk
        chunk = list(takewhile(pred, lines))


def star2(input):
    trans_lines = map(list, zip(*input))
    parts = chunks(trans_lines)

    def apply(row):
        op = ops[row[0][0]]
        nums = map(lambda l: int("".join(l[1:])), row)
        return reduce(op, nums)

    return reduce(operator.add, map(apply, parts))


def main():
    input = read_input("input")
    input = (input[-1], *input[:-1])

    print(f"star1: {star1(input)}")
    print(f"star2: {star2(input)}")


if __name__ == "__main__":
    main()
