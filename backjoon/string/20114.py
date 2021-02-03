import sys
from copy import deepcopy
input = sys.stdin.readline


def join_to_string(x):
    res_c = '?'
    for ch in x:
        if ch != '?':
            res_c = ch
    return res_c


n, h, w = map(int, input().rstrip().split())
str_list = [input().rstrip() for i in range(h)]
result = []

for str_index, str_seq in enumerate(str_list):
    res_arr = []
    for index, c in enumerate(str_seq):
        res_arr.append(c)
        if (index+1) % w == 0:
            result.append(deepcopy(res_arr))
            res_arr = []

    if len(res_arr) > 0:
        result.append(deepcopy(res_arr))

result = list(map(lambda x: join_to_string(x), result))
result = [''.join(result[i:i+n]) for i in range(0, n*h, n)]

res_str = ""
for i in range(n):
    arr = []
    for j in range(h):
        arr.append(result[j][i])
    res_str += join_to_string(arr)

print(res_str)

