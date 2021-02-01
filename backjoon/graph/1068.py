import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
node_list = list(map(int, input().rstrip().split()))
delete = int(input().rstrip())
tree = [[] for _ in range(n)]

for p, q in enumerate(node_list):
    if q == -1:
        continue
    else:
        tree[q].append(p)


def bfs_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue += set(graph[node]) - set(visited)
    return visited


deleted_node = bfs_with_adj_list(tree, delete)
result = 0

for node in tree:
    if node.__contains__(delete):
        node.remove(delete)

for idx, node in enumerate(tree):
    if deleted_node.__contains__(idx):
        continue
    else:
        if len(node) == 0:
            result += 1

print(result)
