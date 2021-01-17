import sys
from itertools import groupby

input = sys.stdin.readline


def max_continuous_length(array):
    return max((sum(1 for _ in g) for k, g in groupby(data)), default=0)


def get_longest_strings(rows):
    for i in range(count):
        column = []
        for j in range(count):
            column.append(rows[j][i])
        rows.append(column)


data = []
count = int(input().rstrip())

for i in range(count):
    candy_str = input().rstrip()
    candy_arr = []
    for candy in candy_str:
        candy_arr.append(candy)
    data.append(candy_arr)

get_longest_strings(data)