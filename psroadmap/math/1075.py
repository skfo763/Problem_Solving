import sys

input = sys.stdin.readline

n = int(input().rstrip())
f = int(input().rstrip())

start = (n // 100) * 100
result = 0

for i in range(start, start + 100):
    if i % f == 0:
        result = i - start
        break

if result // 10 == 0:
    print("0" + str(result))
else:
    print(str(result))
