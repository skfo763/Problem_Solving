import sys
input = sys.stdin.readline
n = int(input().rstrip())
p = list(map(int, input().rstrip().split()))
p.insert(0, 0)

dp = [0 for _ in range(1000+1)]
dp[1] = p[1]

for i in range(2, n+1):
    for j in range(1, i+1):
        if dp[i] == 0:
            dp[i] = dp[i-j] + p[j]
        else:
            dp[i] = min(dp[i], dp[i-j] + p[j])

print(dp[n])
