import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    p, q = map(int, input().rstrip().split())
    graph[p].append(q)
    graph[q].append(p)


def dfs(target_graph, start):
    dfs_deq = deque([start])
    visited = [False] * len(target_graph)
    result = []

    while len(dfs_deq) > 0:
        curr_vertex = dfs_deq.pop()
        if not visited[curr_vertex]:
            result.append(curr_vertex)
            dfs_deq.extend(sorted(graph[curr_vertex], reverse=True))
            visited[curr_vertex] = True
    return result


def bfs(target_graph, start):
    bfs_deq = deque([start])
    visited = [False] * len(target_graph)
    result = []

    while len(bfs_deq) > 0:
        curr_vertex = bfs_deq.popleft()
        visited[curr_vertex] = True
        for target_v in sorted(graph[curr_vertex]):
            if not visited[target_v] and not bfs_deq.__contains__(target_v):
                bfs_deq.append(target_v)
        result.append(curr_vertex)
    return result


print(' '.join(map(str, dfs(graph, v))))
print(' '.join(map(str, bfs(graph, v))))