import sys
input = sys.stdin.readline
print = sys.stdout.write

list = [0 for i in range(10001)]
n = int(input().rstrip())

# 상자에 담는다.
for _ in range(n):
    number = int(input().rstrip())
    list[number] = list[number] + 1

# 상자에 담긴걸 확인하고 출력
for i, val in enumerate(list):
    for j in range(val):
        print(str(i))
        print('\n')