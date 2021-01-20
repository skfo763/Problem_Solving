import sys
input = sys.stdin.readline

num = int(input().rstrip())
dp = [0 for _ in range(21)]
dp[0] = 1
dp[1] = 1

for i in range(2, 21):
    dp[i] = dp[i-1]*i

print(dp[num])