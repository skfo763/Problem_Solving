max = 1000000

start, end = map(int, input().split())
number_list = [True for i in range(max + 1)]
number_list[0] = False
number_list[1] = False

for i in range(2, max+1):
    if not number_list[i]:
        continue

    for j in range(2, max//i + 1):
        number_list[i*j] = False

for i in range(start, end+1):
    if number_list[i]:
        print(i)


