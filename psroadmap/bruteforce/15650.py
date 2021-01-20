import sys
input = sys.stdin.readline


def skip(str_seq, i):
    if len(str_seq) == 0:
        return False
    else:
        return int(str_seq[-1]) >= int(i)


def f(input_list, m):
    if m == 1:
        return input_list
    else:
        l = f(input_list, m-1)
        result = []
        for i in input_list:
            for j in l:
                if skip(j, i):
                    continue
                result.append(j + i)
        return result


n, m = map(int, input().rstrip().split())
num_list = [str(i) for i in range(1, n+1)]

for item in sorted(f(num_list, m)):
    for char in list(item):
        print(char, end=" ")
    print()
