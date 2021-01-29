import sys
input = sys.stdin.readline

count = int(input().rstrip())
time_list = [0 for i in range(count + 1)]
money_list = [0 for i in range(count + 1)]

dp = [0] * (count+2)
for i in range(1, count+1):
    time_list[i], money_list[i] = map(int, input().rstrip().split())

for i in range(1, count+2):
    for j in range(1, i):
        dp[i] = max(dp[i], dp[j])

        if j + time_list[j] == i:
            dp[i] = max(dp[j] + money_list[j], dp[i])

print(max(dp))