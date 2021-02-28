import sys
sys.setrecursionlimit(100000)
n, p, q = map(int, input().split())
dp = [-1]*(10**12)
dp[0] = 1


def f(i, p, q):
    if dp[i] != -1:
        return dp[i]
    else:
        dp[i] = f(i//p, p, q) + f(i//q, p, q)
        return dp[i]

print(f(n, p, q))