import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def f(num, k):
    if k == 0:
        return 0
    else:
        if num >= 10 ** k:
            val = 9 * (10**(k-1))
        else:
            val = num - (10 ** (k-1)) + 1
    return f(num, k-1) + (k * val)


n = input().rstrip()
len_n = len(n)

print(f(int(n), len_n))

