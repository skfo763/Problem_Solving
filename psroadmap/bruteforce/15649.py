import sys
input = sys.stdin.readline


def f(input_list, count):
    if count == 1:
        return input_list
    else:
        temp_list = []
        l = f(input_list, count - 1)
        for i in input_list:
            for j in l:
                if j.__contains__(i):
                    continue
                temp_list.append(j + i)
        return temp_list


n, m = map(int, input().rstrip().split())
num_list = [str(i) for i in range(1, n+1)]
result = sorted(f(num_list, m))

for item in result:
    for j in list(item):
        print(j, end=" ")
    print()