import sys
print = sys.stdout.write
count = int(input())
arr = [[' ']*count for _ in range(count)]


def get_star(row, col, input_count):
    if input_count == 1:
        arr[row][col] = '*'
        return
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            get_star(row + input_count // 3 * i, col + input_count // 3 * j, input_count // 3)


get_star(0, 0, count)

for i in range(count):
    for j in range(count):
        print(arr[i][j])
    print('\n')