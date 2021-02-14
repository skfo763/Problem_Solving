import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
table = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
dp[1][1] = table[0][0]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j == 1:
            continue
        dp[i][j] = dp[i][j-1] + dp[i-1][j] + table[i-1][j-1] - dp[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    add = dp[x2][y2]
    minus = dp[x2][y1-1] + dp[x1-1][y2]
    overlap = dp[x1-1][y1-1]
    print(add - minus + overlap)