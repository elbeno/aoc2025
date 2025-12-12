#!/usr/bin/env python3


def read_input(filename):
    graph = {}

    def add_to_graph(s):
        head, *tail = s.split()
        graph[head[:-1]] = tail

    with open(filename, "r") as f:
        for line in f:
            add_to_graph(line)

    return graph


def star1(graph):
    ways = 0
    q = ["you"]
    while len(q) != 0:
        head, *q = q
        if head == "out":
            ways += 1
        elif head in graph:
            q.extend(graph[head])
    return ways


def star2(graph):
    return 0


def main():
    graph = read_input("input")
    print(f"star1: {star1(graph)}")
    print(f"star2: {star2(graph)}")


if __name__ == "__main__":
    main()
