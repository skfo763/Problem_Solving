import sys
from collections import deque
from itertools import groupby
input = sys.stdin.readline

count = int(input().rstrip())
house_map = [list(input().rstrip()) for _ in range(count)]
has_child = [False] * (count**2)
graph = [[] for _ in range(count**2)]
conn_graph = [-1] * (count**2)

for i in range(len(house_map)):
    for j in range(len(house_map)):
        if house_map[i][j] != '0':
            curr = (i * count) + j
            has_child[curr] = True
            top = i-1
            bottom = i+1
            left = j-1
            right = j+1

            if top >= 0 and house_map[top][j] != '0':
                graph[curr].append(top*count + j)
            if bottom < count and house_map[bottom][j] != '0':
                graph[curr].append(bottom*count + j)
            if left >= 0 and house_map[i][left] != '0':
                graph[curr].append(i*count + left)
            if right < count and house_map[i][right] != '0':
                graph[curr].append(i*count + right)


def bfs(input_graph, start):
    bfs_deque = deque([start])
    visited = [False]*len(input_graph)
    result = []
    while len(bfs_deque) > 0:
        curr_node = bfs_deque.pop()
        visited[curr_node] = True
        for target_node in input_graph[curr_node]:
            if not visited[target_node] and not bfs_deque.__contains__(target_node):
                bfs_deque.appendleft(target_node)
        result.append(curr_node)
    return result


for i in range(len(has_child)):
    if not has_child[i]:
        continue
    if conn_graph[i] == -1:
        bfs_result = bfs(graph, i)
        for each_node in bfs_result:
            conn_graph[each_node] = i

conn_graph = sorted(list(filter(lambda x: x >= 0, conn_graph)))
conn_graph = sorted([len(list(group)) for key, group in groupby(conn_graph)])

print(len(conn_graph))
for count in conn_graph:
    print(count)