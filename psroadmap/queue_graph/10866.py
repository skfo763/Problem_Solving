import sys


class Deque:
    def __init__(self):
        self.deque = []

    def push_front(self, x):
        self.deque.insert(0, x)

    def push_back(self, x):
        self.deque.append(x)

    def pop_front(self):
        if len(self.deque) <= 0:
            return -1
        else:
            result = self.deque.pop(0)
            return result

    def pop_back(self):
        if len(self.deque) <= 0:
            return -1
        else:
            result = self.deque.pop(len(self.deque) - 1)
            return result

    def size(self):
        return len(self.deque)

    def empty(self):
        return self.size() <= 0

    def front(self):
        if len(self.deque) <= 0:
            return -1
        else:
            return self.deque[0]

    def back(self):
        if len(self.deque) <= 0:
            return -1
        else:
            return self.deque[-1]


input = sys.stdin.readline
count = int(input().rstrip())
deque = Deque()

for i in range(count):
    cmd = input().rstrip().split()
    if cmd[0] == 'push_front':
        deque.push_front(cmd[1])
    elif cmd[0] == 'push_back':
        deque.push_back(cmd[1])
    elif cmd[0] == 'pop_front':
        print(deque.pop_front())
    elif cmd[0] == 'pop_back':
        print(deque.pop_back())
    elif cmd[0] == 'size':
        print(deque.size())
    elif cmd[0] == 'empty':
        print(1 if deque.empty() else 0)
    elif cmd[0] == 'front':
        print(deque.front())
    elif cmd[0] == 'back':
        print(deque.back())
