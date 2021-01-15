import sys

input = sys.stdin.readline

index = int(input().rstrip())
n = index
start = 1

while n - start > 0:
    n -= start
    start += 1

start_index = 1
for i in range(1, start):
    start_index += i

number = start + 1
if start % 2 == 0:
    for i in range(0, start):
        if start_index + i == index:
            child = i+1
            parent = number - child
            print("%d/%d" % (child, parent))
else:
    for i in range(start, 0, -1):
        if start_index + start - i == index:
            print("%d/%d" % (i, number-i))