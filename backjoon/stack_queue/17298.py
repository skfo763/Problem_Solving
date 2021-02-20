from collections import deque

count = int(input())
data = list(map(int, input().rstrip().split()))
a = deque()
b = deque()
result = []

for num in data:
    a.append(num)

while len(a) > 0:
    atop = a.pop()
    if len(b) == 0:
        result.append(-1)
        b.append(atop)
    else:
        num = -1
        while len(b) > 0:
            btop = b[-1]
            if btop > atop:
                num = btop
                break
            b.pop()
        result.append(num)
        b.append(atop)

for num in list(reversed(result)):
    print(num)


