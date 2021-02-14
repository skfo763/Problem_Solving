import sys
input = sys.stdin.readline

n = int(input().rstrip())
box = list(map(int, input().rstrip().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(0, i):
        if box[j] < box[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
