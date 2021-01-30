import sys

input = sys.stdin.readline

count = int(input().rstrip())
data = [int(input().rstrip()) for _ in range(count)]
data = sorted(data, reverse=True)
result = False

for i in range(len(data) - 2):
    if data[i] < data[i + 1] + data[i + 2]:
        print(data[i] + data[i + 1] + data[i + 2])
        result = True
        break

if not result:
    print(-1)
