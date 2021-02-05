import sys
from collections import deque
max = 100001
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
line = [max for i in range(max)]
visited = [False for _ in range(max)]
queue = deque([n])
line[n] = 0

while len(queue) > 0:
    curr = queue.pop()
    visited[curr] = True

    if 0 <= curr-1 < max and not visited[curr-1]:
        queue.appendleft(curr-1)
        line[curr-1] = min(line[curr-1], line[curr] + 1)
    if 0 <= curr+1 < max and not visited[curr+1]:
        queue.appendleft(curr+1)
        line[curr + 1] = min(line[curr+1], line[curr] + 1)
    if 0 <= curr*2 < max and not visited[curr*2]:
        queue.appendleft(curr*2)
        line[curr*2] = min(line[curr*2], line[curr] + 1)

print(line[k])