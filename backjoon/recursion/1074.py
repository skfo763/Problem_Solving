import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def func(k, x, y):
    if k == 0:
        return 0
    else:
        x_pos = 1 if x // 2**(k-1) > 0 else 0
        y_pos = 1 if y // 2**(k-1) > 0 else 0
        x_mod = x % 2**(k-1)
        y_mod = y % 2**(k-1)

        pos = 1
        if x_pos == 0 and y_pos == 0:
            pos = 0
        elif x_pos == 0 and y_pos == 1:
            pos = 1
        elif x_pos == 1 and y_pos == 0:
            pos = 2
        elif x_pos == 1 and y_pos == 1:
            pos = 3
        val = pos * (4 ** (k-1))
        return func(k-1, x_mod, y_mod) + val


n, r, c = map(int, input().rstrip().split())
start = 0
print(func(n, r, c))
