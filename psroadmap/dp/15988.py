import sys
input = sys.stdin.readline
divisor = 1000000009

dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = ((dp[i-1] % divisor) + (dp[i-2] % divisor) + (dp[i-3] + divisor)) % divisor

count = int(input().rstrip())

for i in range(count):
    num = int(input().rstrip())
    print(dp[num])