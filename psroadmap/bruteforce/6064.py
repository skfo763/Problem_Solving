import sys
input = sys.stdin.readline


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def lcm(a, b):
    return (a*b) // gcd(a, b)


def get_year(m, n, x, y):
    cnt = x % (m + 1)
    tempY = x
    is_valid = False
    for j in range(n):
        ty = n if tempY % n == 0 else (tempY % n)
        if ty == y:
            is_valid = True
            break
        cnt += m
        tempY = ty + m
    return cnt if is_valid else -1


count = int(input().rstrip())
for i in range(count):
    m, n, x, y = map(int, input().rstrip().split())
    print(get_year(m, n, x, y))
