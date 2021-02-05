from collections import deque

def bfs():
    q = deque()
    q.append(n)
    ans, cnt = 0, 0
    while not cnt:
        s = len(q)
        while s:
            s -= 1
            x = q.popleft()
            if x == k:
                cnt += 1
            for nx in (x-1, x+1, x*2):
                if nx < 0 or nx > MAX:
                    continue
                if not dist[nx] or dist[nx] == dist[x]+1:
                    dist[nx] = dist[x]+1
                    q.append(nx)
        ans += 1
    print("%d\n%d" % (ans-1, cnt))

MAX = 100000
n, k = map(int, input().split())
dist = [0]*(MAX+1)
bfs()