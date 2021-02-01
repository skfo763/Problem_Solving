import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n)]
visited = [False] * n

for i in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(index, depth):
    if depth == 4:
        print(1)
        exit()
    else:
        for node in graph[index]:
            if not visited[node]:
                visited[node] = True
                dfs(node, depth + 1)
                visited[node] = False


for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)
