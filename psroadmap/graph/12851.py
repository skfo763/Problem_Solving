import sys
from collections import deque
n, k = list(map(int, sys.stdin.readline().split()))


def bfs(n, k):
    if n == k:
        return 0, 1
    if n > k:
        return n-k, 1

    # visited[j] : j 까지 오는데 얼마의 최소 time을 저장.
    # ways[j] : j 까지 최소 time으로 오는 방법의 수 저장.
    q, visited, ways = deque([n]), [float('inf')]*100001, [0]*100001
    time, count, success = 0, 0, False
    ways[n] = 1
    visited[n] = 0
    while q and not success:
        size = len(q)
        for _ in range(size):
            cur = q.popleft()
            next_move = [cur-1, cur+1, cur*2]
            for j in next_move:
                if 0 <= j <= 100000 and time + 1 <= visited[j]:
                    ways[j] += 1
                    visited[j] = time + 1
                    if j == k:
                        success = True
                    if not success:
                        q.append(j)
        time += 1
    return visited[k], ways[k]


time, count = bfs(n, k)
print(time)
print(count) 