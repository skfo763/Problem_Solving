import sys
import copy
input = sys.stdin.readline


def f(input_list, k):
    if k == 1:
        return list(map(lambda x: [x], input_list))
    else:
        prev_list = f(input_list, k-1)
        res = []
        for num in prev_list:
            for i in input_list:
                if num[-1] >= i:
                    continue
                else:
                    temp_num = copy.deepcopy(num)
                    temp_num.append(i)
                    res.append(temp_num)
        return res


m, n = map(int, input().rstrip().split())
data = sorted(list(map(int, input().rstrip().split())))

result = f(data, n)
for s in result:
    for k in s:
        print(k, end=" ")
    print()
