from collections import deque

count = int(input())
queue = deque()
for i in range(1, count+1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    newtop = queue.popleft()
    queue.append(newtop)

print(queue[0])