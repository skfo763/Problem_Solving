import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maze = [list(map(int, list(input().rstrip()))) for _ in range(n)]
maze_deq = deque([[0, 0]])
dist = [[2000000 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dist[0][0] = 0

while len(maze_deq) > 0:
    curr_pos = maze_deq.pop()
    i = curr_pos[0]
    j = curr_pos[1]

    top = i - 1
    bottom = i + 1
    left = j - 1
    right = j + 1
    temp_dist = dist[i][j]
    visited[i][j] = True

    if top >= 0 and not visited[top][j] and maze[top][j] != 0:
        maze_deq.appendleft([top, j])
        dist[top][j] = min(dist[top][j], temp_dist+1)
    if bottom < n and not visited[bottom][j] and maze[bottom][j] != 0:
        maze_deq.appendleft([bottom, j])
        dist[bottom][j] = min(dist[bottom][j], temp_dist + 1)
    if left >= 0 and not visited[i][left] and maze[i][left] != 0:
        maze_deq.appendleft([i, left])
        dist[i][left] = min(dist[i][left], temp_dist + 1)
    if right < m and not visited[i][right] and maze[i][right] != 0:
        maze_deq.appendleft([i, right])
        dist[i][right] = min(dist[i][right], temp_dist + 1)

print(dist[n-1][m-1] + 1)