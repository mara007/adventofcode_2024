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

    similarity_score = 0
    for n in list1:
        similarity_score += n * list2.count(n)

    return similarity_score


if __name__ == '__main__':
    INPUT_FILE = 'day_1_historian_hysterya.txt'
    similarity_score = solve(INPUT_FILE)
    print(f'{similarity_score=}')

