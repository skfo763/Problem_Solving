import sys
num = int(input().rstrip())
dp = [0 for i in range(21)]
dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(3, 21):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[num])
