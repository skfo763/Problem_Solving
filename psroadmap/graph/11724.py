import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    p, q = map(int, input().rstrip().split())
    graph[p].append(q)
    graph[q].append(p)


def bfs(input_graph, start):
    bfs_deq = deque([start])
    visited = [False] * (n + 1)
    result = []

    while len(bfs_deq) > 0:
        curr_node = bfs_deq.pop()
        visited[curr_node] = True
        for target_node in input_graph[curr_node]:
            if not visited[target_node] and not bfs_deq.__contains__(target_node):
                bfs_deq.appendleft(target_node)
        result.append(curr_node)
    return result


res = 0
connect_component = [-1 for _ in range(n + 1)]
for i in range(1, n + 1):
    if connect_component[i] == -1:
        bfs_result = bfs(graph, i)
        for node in bfs_result:
            connect_component[node] = i

print(len(set(connect_component[1:n + 1])))
