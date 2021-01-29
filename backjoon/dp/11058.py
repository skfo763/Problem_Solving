import sys

input = sys.stdin.readline

k = int(input())
dp = [0 for _ in range(101)]
for i in range(0, 6):
    dp[i] = i

for i in range(6, 101):
    dp[i] = max(dp[i - 1] + 1, dp[i - 3] * 2, dp[i - 4] * 3, dp[i - 5] * 4)

print(dp[k])
