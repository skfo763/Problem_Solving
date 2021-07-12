n = int(input())
start = list(map(int, input().split()))
finish = list(map(int, input().split()))

"""
road = [True for _ in range(n+1)]

for i in range(len(start)):
    go = start[i]
    stop = finish[i]
    for j in range(go, stop+1):
        road[j] = False

result = 0
temp_result = 0

for i in range(1, len(road)):
    if not road[i]:
        result = max(result, temp_result)
        temp_result = 0
        continue
    temp_result += 1

print(result)

"""

result = 0
min_start = 0
for i in range(1, len(start)):
    if finish[min_start] > start[i] and start[i] < start[min_start]:
        result = 0
        min_start = i
    elif finish[min_start] < start[i]:
        result = max(result, (start[i] - finish[min_start]) - 1)
        min_start = i

if n - max(finish) > result:
    result = n - max(finish)
if min(start) - 1 > result:
    result = min(start) - 1

print(result)
