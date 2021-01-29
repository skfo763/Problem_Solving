import sys
from copy import deepcopy
sys.setrecursionlimit(100000)
input = sys.stdin.readline
number_list = [i for i in range(-10, 11)]


def available_num_list(input_k):
    if input_k == 1:
        return list(map(lambda x: [x], number_list))
    else:
        prev = available_num_list(input_k - 1)
        result = []
        for arr in prev:
            for num in number_list:
                temp_arr = deepcopy(arr)
                temp_arr.append(num)
                result.append(temp_arr)
        return result


k = int(input())
combination_set = [tuple(item) for item in available_num_list(k)]
combination_set = set(combination_set)

for comb in sorted(combination_set):
    print(comb)