n, m = map(int, input().split())
card = list(map(int, input().split()))

res = 0
for i in range(0, n-2):
    for j in range(1, n-1):
        for k in range(2, n):
            if i == j or j == k or i == k:
                continue
            add_res = card[i] + card[j] + card[k]
            if res < add_res <= m:
                res = add_res
print(res)
