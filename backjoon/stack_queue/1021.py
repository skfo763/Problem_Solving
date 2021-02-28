from collections import deque

n, m = map(int, input().split())
data = list(map(int, input().split()))
queue = deque(range(1, n+1))

res = 0
for target in data:
    if queue[0] == target:
        queue.popleft()
        continue

    target_index = queue.index(target)

    if target_index > len(queue) // 2:
        queue.rotate(len(queue) - target_index)
        res += (len(queue) - target_index)
    elif target_index <= len(queue) // 2:
        queue.rotate(-target_index)
        res += target_index
    queue.popleft()

print(res)





