#!/usr/bin/env python3

def read_input(filename: str):
    result1 = []
    result2 = []

    with open(filename, 'r') as input:
        lines = input.readlines()
        for l in lines:
            pair = l.split('   ')
            assert len(pair) == 2, f'unexpected line: "{pair}"'
            result1.append(int(pair[0]))
            result2.append(int(pair[1]))

    return result1, result2


def solve(filename: str):
    list1, list2 = read_input(filename)
    list1.sort()
    list2.sort()

    total_dist = 0
    for pair in zip(list1, list2):
        total_dist += abs(pair[0] - pair[1])

    return total_dist


if __name__ == '__main__':
    INPUT_FILE = 'day_1_historian_hysterya.txt'
    total_distance_between_lists = solve(INPUT_FILE)
    print(f'{total_distance_between_lists=}')

