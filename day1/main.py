#!/usr/bin/env python3


def read_input(filename):
    def convert(s):
        return int(s.replace("L", "-").replace("R", "+"))

    with open(filename, "r") as f:
        return [convert(line) for line in f]


def scan(f, seq, init):
    yield init
    for value in seq:
        init = f(init, value)
        yield init


def rotate(acc, amount):
    return acc + amount


def star1(rotations, pos):
    return sum(x % 100 == 0 for x in scan(rotate, rotations, pos))


def zero_crossings(x, y):
    cross = abs(y // 100 - x // 100)
    sign = (y >= x) * 2 - 1
    if x % 100 == 0:
        cross += 1/2 * sign
    if y % 100 == 0:
        cross -= 1/2 * sign
    return abs(cross)


def star2(rotations, pos):
    positions = list(scan(rotate, rotations, pos))
    return int(sum(zero_crossings(x, y) for x, y in zip(positions[:-1], positions[1:])))


def main():
    rotations = read_input("input")
    print(f"star1: {star1(rotations, 50)}")
    print(f"star2: {star2(rotations, 50)}")


if __name__ == "__main__":
    main()
