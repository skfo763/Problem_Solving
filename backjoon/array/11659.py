import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
table = list(map(int, input().rstrip().split()))
prefix_sum = [0 for _ in range(n+1)]
prefix_sum[1] = table[0]

for i in range(2, n+1):
    prefix_sum[i] = prefix_sum[i-1] + table[i-1]

for _ in range(m):
    i, j = map(int, input().rstrip().split())
    print(prefix_sum[j] - prefix_sum[i-1])
