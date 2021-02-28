import sys
from collections import deque
input = sys.stdin.readline
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def get_field(m, n, k):
    field = [[0] * m for _ in range(n)]
    for i in range(1, k+1):
        x, y = map(int, input().rstrip().split())
        field[y][x] = i
    return field


def get_graph(field, m, n, k):
    graph = [[] for _ in range(k+1)]
    for i in range(n):
        for j in range(m):
            if field[i][j] == 0:
                continue
            for d in range(4):
                if 0 <= i+di[d] < n and 0 <= j+dj[d] < m and field[i+di[d]][j+dj[d]] != 0:
                    graph[field[i][j]].append(field[i+di[d]][j+dj[d]])
    return graph


def bfs(visited, graph, i):
    queue = deque([i])
    visited[i] = True

    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True


def connected_component(graph):
    visited = [False] * len(graph)
    result = 0
    for i in range(1, len(graph)):
        if visited[i]:
            continue
        bfs(visited, graph, i)
        result += 1
    return result


def solve():
    m, n, k = map(int, input().rstrip().split())
    field = get_field(m, n, k)
    graph = get_graph(field, m, n, k)
    print(connected_component(graph))


t = int(input().rstrip())
for _ in range(t):
    solve()