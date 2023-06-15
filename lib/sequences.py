#!/usr/bin/env python3


def print_fibonacci(length):
    sequence = []
    for n in range(0, length):
        if n < 2:
            sequence.append(n)
        else:
            sequence.append(sequence[n-1] + sequence[n-2])
    print(sequence)