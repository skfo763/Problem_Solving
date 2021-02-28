n = int(input())
max = 10987654321

min = max
t = 0
for i in range(1, n+1):
    res = i + sum(map(int, list(str(i))))
    if res == n and res < min:
        min = res
        t = i

print(t)