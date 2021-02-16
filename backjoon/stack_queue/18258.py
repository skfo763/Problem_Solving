from collections import deque
import sys

input = sys.stdin.readline

count = int(input().rstrip())
queue = deque()
for _ in range(count):
    command = input().rstrip().split()

    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print("-1")
    elif command[0] == 'size':
        print(str(len(queue)))
    elif command[0] == 'empty':
        if queue:
            print('0')
        else:
            print('1')
    elif command[0] == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print("-1")
    elif command[0] == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print("-1")
