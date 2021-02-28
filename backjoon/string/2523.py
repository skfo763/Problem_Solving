n = int(input())

for i in range(1, 2*n):
    if i == n:
        print('*' * n)
    elif i > n:
        print('*' * (2*n-i))
    else:
        print('*' * i)



