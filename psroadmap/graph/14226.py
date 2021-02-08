import sys
from collections import deque
input = sys.stdin.readline
max = 1001

count = int(input().rstrip())
emoticons = [[-1 for _ in range(max)] for _ in range(max)]
emoticons[1][0] = 0
queue = deque([(1, 0)])

while queue:
    s_count, c_count = queue.popleft()

    if emoticons[s_count][s_count] == -1:
        emoticons[s_count][s_count] = emoticons[s_count][c_count] + 1
        queue.append((s_count, s_count))

    if s_count + c_count <= count and emoticons[s_count + c_count][c_count] == -1:
        emoticons[s_count+c_count][c_count] = emoticons[s_count][c_count] + 1
        queue.append((s_count+c_count, c_count))

    if s_count - 1 >= 0 and emoticons[s_count-1][c_count] == -1:
        emoticons[s_count-1][c_count] = emoticons[s_count][c_count] + 1
        queue.append((s_count-1, c_count))

result = filter(lambda x: x != -1, emoticons[count])
print(min(result))