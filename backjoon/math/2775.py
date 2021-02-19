max = 15
apart = [[0]*max for _ in range(max)]

for i in range(0, max):
    if i == 0:
        for j in range(1, max):
            apart[i][j] = j
    else:
        for j in range(1, max):
            if j == 1:
                apart[i][j] = 1
            else:
                for k in range(1, j+1):
                    apart[i][j] += apart[i-1][k]

count = int(input())
for _ in range(count):
    k = int(input())
    n = int(input())
    print(apart[k][n])