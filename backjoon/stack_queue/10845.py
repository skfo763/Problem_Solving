import sys

input = sys.stdin.readline
queue = []


def push(value):
    queue.append(value)


def pop():
    return queue.pop(0) if len(queue) > 0 else -1


def size():
    return len(queue)


def empty():
    return int(len(queue) <= 0)


def front():
    return queue[0] if len(queue) > 0 else -1


def back():
    return queue[-1] if len(queue) > 0 else -1


count = int(input().strip())

for i in range(count):
    command = input().strip().split()
    if command[0] == "push":
        push(command[1])
    elif command[0] == "front":
        print(front())
    elif command[0] == "pop":
        print(pop())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        print(empty())
    elif command[0] == "back":
        print(back())
    else:
        print("illegal command")
