import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def pow(a, k, m):
    if k == 1:
        return a % m
    res = pow(a, k // 2, m)
    res = res * res % m
    if k % 2 == 0:
        return res
    else:
        return res * a % m


a, b, c = map(int, input().rstrip().split())
print(pow(a, b, c))
