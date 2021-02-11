import sys
input = sys.stdin.readline
max = 1000001

count = int(input().rstrip())
dp = [max]*max
path = [0]*max

dp[0] = dp[1] = 0
dp[2] = dp[3] = 1

path[1] = 0
path[2] = path[3] = 1

if count == 1:
    print(0)
    print(1)
    exit()

for i in range(4, max):
    min_val = dp[i-1]
    index = i-1

    if i % 2 == 0 and min_val > dp[i//2]:
        min_val = dp[i//2]
        index = i//2

    if i % 3 == 0 and min_val > dp[i//3]:
        min_val = dp[i//3]
        index = i//3

    dp[i] = dp[index] + 1
    path[i] = index

target_path = [count]
curr = path[count]

while curr != 1:
    target_path.append(curr)
    curr = path[curr]

target_path.append(1)
print(dp[count])
for num in target_path:
    print(num, end=" ")
