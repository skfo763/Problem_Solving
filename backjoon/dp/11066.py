import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
inf = 1110987654321


def solve():
    k = int(input())
    page = [0] + list(map(int, input().rstrip().split()))
    cu_sum = [0] * (k+1)
    cache = [[-1] * (k+1) for _ in range(k+1)]
    for i in range(1, k+1):
        cu_sum[i] = cu_sum[i-1] + page[i]
    print(f(cache, page, cu_sum, 1, k))


def f(cache, page, cu_sum, i, j):
    if i == j:
        return 0

    if cache[i][j] != -1:
        return cache[i][j]

    sum = cu_sum[j] - cu_sum[i-1]
    res = inf
    for k in range(0, j-i):
        res = min(res, f(cache, page, cu_sum, i, i+k) + f(cache, page, cu_sum, i+k+1, j))

    cache[i][j] = res + sum
    return cache[i][j]


t = int(input().rstrip())
for _ in range(t):
    solve()