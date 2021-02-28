from collections import deque
di = [-1, 1, 0, 0, 0, 0]
dj = [0, 0, -1, 1, 0, 0]
dk = [0, 0, 0, 0, -1, 1]

m, n, h = map(int, input().split())
boxes = []
for _ in range(h):
    boxes.append([list(map(int, input().split())) for _ in range(n)])

bfs_queue = deque()
fast_close = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 1:
                bfs_queue.append((i, j, k))

while bfs_queue:
    ci, cj, ck = bfs_queue.popleft()
    curr_date = boxes[ci][cj][ck]
    for i in range(len(di)):
        ni = ci + di[i]
        nj = cj + dj[i]
        nk = ck + dk[i]
        if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m and boxes[ni][nj][nk] == 0:
            boxes[ni][nj][nk] = curr_date + 1
            bfs_queue.append((ni, nj, nk))

res = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 0:
                print(-1)
                exit()
            elif boxes[i][j][k] > res:
                res = boxes[i][j][k]

print(res-1)