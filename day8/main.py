#!/usr/bin/env python3

import operator
from functools import reduce


def read_input(filename):
    def convert(s):
        return [int(n) for n in s.split(",")]

    with open(filename, "r") as f:
        return [convert(line) for line in f]


def distance(b1, b2):
    return reduce(operator.add, map(lambda x, y: pow(abs(y - x), 2), b1, b2), 1)


def compute_distances(input):
    distances = []
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            distances.append([i, j, distance(input[i], input[j])])
    distances.sort(key=lambda x: x[2])
    return distances


def add_connection(x, connections):
    idx_i = None
    idx_j = None
    
    for n,c in enumerate(connections):
        if x[0] in c:
            idx_i = n
            break
    for n,c in enumerate(connections):
        if x[1] in c:
            idx_j = n
            break

    if idx_i is None and idx_j is None:
        connections.append({x[0], x[1]})
        
    if idx_i == idx_j:
        return
    
    if idx_i is not None and idx_j is not None:
        connections[idx_i] |= connections[idx_j]
        del connections[idx_j]
        return
    
    if idx_i is not None:
        connections[idx_i].add(x[1])
    else:
        connections[idx_j].add(x[0])
                
    

def star1(input, distances, num_conns):
    connections = []
    for i in range(num_conns):
        add_connection(distances[i], connections)

    l = list(connections)
    l.sort(key=len, reverse=True)
        
    return reduce(operator.mul, (len(x) for x in l[:3]), 1)


def main():
    input = read_input("input")
    distances = compute_distances(input)
    print(f"star1: {star1(input, distances, 1000)}")


if __name__ == "__main__":
    main()
