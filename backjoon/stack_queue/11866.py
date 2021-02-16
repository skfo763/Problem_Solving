from collections import deque

queue = deque()
n, k = map(int, input().split())

for i in range(1, n+1):
    queue.append(i)

result = []
while queue:
    for i in range(k):
        num = queue.popleft()
        if i == k-1:
            result.append(num)
        else:
            queue.append(num)


result = list(map(lambda x: str(x), result))
print("<", end="")
print(", ".join(result), end="")
print(">", end="")