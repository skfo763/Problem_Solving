import sys
input = sys.stdin.readline

count = int(input().strip())
stack = []


def push(value):
    stack.append(value)


def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]


def size():
    return len(stack)


def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()


def empty():
    return int(len(stack) <= 0)


for i in range(count):
    command = input().strip().split()
    if command[0] == "push":
        push(command[1])
    elif command[0] == "top":
        print(top())
    elif command[0] == "pop":
        print(pop())
    elif command[0] == "size":
        print(size())
    elif command[0] == "empty":
        print(empty())
    else:
        print("illegal command")
