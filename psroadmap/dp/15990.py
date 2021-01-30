import sys
input = sys.stdin.readline
divisor = 1000000009

dp = [[0 for _ in range(4)] for _ in range(100001)]
dp[1][1] = dp[2][2] = dp[3][1] = dp[3][2] = dp[3][3] = 1

for i in range(4, 100001):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % divisor
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % divisor
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % divisor

count = int(input().rstrip())

for i in range(count):
    num = int(input().rstrip())
    result = (dp[num][1] + dp[num][2] + dp[num][3]) % divisor
    print(result)




