"""
dp[i][j] = i번째 수까지 이용해서 j를 만드는 경우의 수

-> number_list = [1, 2, 3] 일 때
dp[1][0] = 0
dp[1][1] = 1
dp[1][2] = 0
...
dp[1][20] = 0
---
dp[i][j] =>
i-1번째 수 까지 이용해서 0~20 사이의 j+n[i] / j-n[i] 을 만들 수 있는 경우의 수

number_list[2] = 2
dp[2][0] => dp[1][2]
dp[2][1] => dp[1][3]
dp[2][2] => dp[1][0] + dp[1][4]
dp[2][3] => dp[1][1] + dp[1][5]
...

for i, value in number_list:
    for i in 0~20:
        if 0 <= j + n[i] <= 20:
            dp[i][j] += dp[i-1][j+n[i]]
        if 0 <= j - n[i] <= 20:
            dp[i][j] += dp[i-1[j-n[i]]
"""
import sys
input = sys.stdin.readline

count = int(input().rstrip())
n = list(map(int, input().rstrip().split()))

dp = [[0 for _ in range(22)] for _ in range(101)]
dp[0][n[0]] = 1

for i in range(1, count):
    for j in range(21):
        if 0 <= j + n[i] <= 20:
            dp[i][j] += dp[i - 1][j + n[i]]
        if 0 <= j - n[i] <= 20:
            dp[i][j] += dp[i - 1][j - n[i]]

print(dp[count - 2][n[count - 1]])
