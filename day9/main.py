#!/usr/bin/env python3


def read_input(filename):
    def convert(s):
        return [int(n) for n in s.split(",")]

    with open(filename, "r") as f:
        return [convert(line) for line in f]


def area(b1, b2):
    return (abs(b1[0] - b2[0]) + 1) * (abs(b1[1] - b2[1]) + 1)


def compute_areas(input):
    distances = []
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            distances.append([i, j, area(input[i], input[j])])
    distances.sort(key=lambda x: x[2], reverse=True)
    return distances


def star1(input):
    areas = compute_areas(input)
    return areas[0][2]


def main():
    input = read_input("input")
    print(f"star1: {star1(input)}")


if __name__ == "__main__":
    main()
