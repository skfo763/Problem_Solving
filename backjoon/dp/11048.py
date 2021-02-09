import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maze = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = maze[0][0]

for i in range(n):
    for j in range(m):
        candidates = []
        if i-1 >= 0:
            candidates.append(dp[i-1][j])

        if j-1 >= 0:
            candidates.append(dp[i][j-1])

        if i-1 >= 0 and j-1 >= 0:
            candidates.append(dp[i-1][j-1])

        if len(candidates) == 0:
            dp[i][j] = maze[i][j]
        else:
            dp[i][j] = max(candidates) + maze[i][j]

print(dp[n-1][m-1])