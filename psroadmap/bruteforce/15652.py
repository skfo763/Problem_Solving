import sys
input = sys.stdin.readline


def f(input_list, k):
    if k == 1:
        return input_list
    else:
        temp_list = f(input_list, k-1)
        result = []
        for num in temp_list:
            for i in input_list:
                if num[-1] > i:
                    continue
                else:
                    result.append(num + i)
        return result


a, b = map(int, input().rstrip().split())
data = []
for i in range(1, a+1):
    data.append(str(i))

result = sorted(set(f(data, b)))

for num in result:
    for char in list(num):
        print(char, end=" ")
    print()

