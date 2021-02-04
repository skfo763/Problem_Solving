import sys
from collections import deque

input = sys.stdin.readline
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def init_rotten_tomato(tomato_box, m, n):
    res_deq = deque()
    for i in range(n):
        for j in range(m):
            if tomato_box[i][j] == 1:
                res_deq.append([i, j])
    return res_deq


def bfs(tomato_box, deq, m, n):
    while len(deq) > 0:
        i, j = deq.popleft()
        for k in range(4):
            target_i = i + di[k]
            target_j = j + dj[k]

            if 0 <= target_i < n and 0 <= target_j < m and tomato_box[target_i][target_j] == 0:
                tomato_box[target_i][target_j] = tomato_box[i][j] + 1
                deq.append([target_i, target_j])


m, n = map(int, input().rstrip().split())
box = [list(map(int, input().rstrip().split())) for _ in range(n)]
bfs_deque = init_rotten_tomato(box, m, n)

bfs(box, bfs_deque, m, n)

max_val = -2
is_ok = False
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            is_ok = True
        max_val = max(max_val, box[i][j])

if is_ok:
    print(-1)
elif max_val == -1:
    print(0)
else:
    print(max_val-1)
