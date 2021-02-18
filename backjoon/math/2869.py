import math

a, b, v = map(int, input().split())

prev = v - a
one_day = a - b

if a == v:
    print(1)
elif one_day >= prev:
    print(2)
else:
    print(math.ceil(prev/one_day) + 1)