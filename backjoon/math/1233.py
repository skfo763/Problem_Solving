import sys

input = sys.stdin.readline

a, b, c = map(int, input().rstrip().split())
result_distribution = [0 for i in range(81)]

for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            add = i + j + k
            result_distribution[add] += 1

max_value = max(result_distribution)
print(result_distribution.index(max_value))
