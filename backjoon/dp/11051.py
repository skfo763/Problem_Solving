import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
dp = [0 for i in range(10001)]
dp[0] = dp[1] = 1

for i in range(2, 10001):
    dp[i] = dp[i-1]*i

result = (dp[n] // (dp[k] * dp[n-k])) % 10007
print(result)