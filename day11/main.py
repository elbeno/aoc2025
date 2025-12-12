#!/usr/bin/env python3

from functools import cache


def read_input(filename):
    graph = {}

    def add_to_graph(s):
        head, *tail = s.split()
        graph[head[:-1]] = tail

    with open(filename, "r") as f:
        for line in f:
            add_to_graph(line)

    return graph


graph_g = read_input("input")


def star1():
    ways = 0
    q = ["you"]
    while len(q) != 0:
        head, *q = q
        if head == "out":
            ways += 1
        elif head in graph_g:
            q.extend(graph_g[head])
    return ways


@cache
def num_ways(start, end):
    if start not in graph_g:
        return 0
    if end in graph_g[start]:
        return 1
    return sum(num_ways(n, end) for n in graph_g[start])


def star2():
    return num_ways("svr", "fft") * num_ways("fft", "dac") * num_ways(
        "dac", "out"
    ) + num_ways("svr", "dac") * num_ways("dac", "fft") * num_ways("fft", "out")


def main():
    print(f"star1: {star1()}")
    print(f"star2: {star2()}")


if __name__ == "__main__":
    main()
