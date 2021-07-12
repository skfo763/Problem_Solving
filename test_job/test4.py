from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def get_graph(v):
    n = len(v)
    m = len(v[0])
    graph = [[] for _ in range(n * m)]

    for i in range(n):
        for j in range(m):
            if v[i][j] == 0:
                continue
            for d in range(4):
                if 0 <= i + di[d] < n and 0 <= j + dj[d] < m and v[i + di[d]][j + dj[d]] != 0:
                    graph[(i * m) + j].append((i + di[d]) * m + j + dj[d])

    return graph


def bfs(visited, graph, i):
    queue = deque([i])
    visited[i] = True
    result = 0

    while queue:
        curr = queue.popleft()
        result += 1
        for next in graph[curr]:
            if next != [-1] and not visited[next]:
                queue.append(next)
                visited[next] = True
    return result


def connected_component(graph, field):
    visited = [False] * len(graph)
    result = []

    for i in range(len(graph)):
        length = len(field[0])
        n_i = i // length
        n_j = i % length
        k = field[n_i][n_j]
        if visited[i] or k != 1:
            continue
        result.append(bfs(visited, graph, i))

    if len(result) == 0:
        return [0, 0]
    else:
        return [len(result), max(result)]


def solution(v):
    graph = get_graph(v)
    result = connected_component(graph, v)
    return result

v = [[0]]
print(solution(v))