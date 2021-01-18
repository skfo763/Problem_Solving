import sys


def check_continuous_char(input_array):
    res = 1
    current_count = 1
    current_char = input_array[0]

    for char in input_array[1:]:
        if current_char == char:
            current_count += 1
        else:
            if res < current_count:
                res = current_count
            current_char = char
            current_count = 1
    if res < current_count:
        res = current_count
    return res


def flatten_2d_array(input_array):
    flatten = []
    for row in input_array:
        flatten.append(row)
    for i in range(len(input_array)):
        line = []
        for j in range(len(input_array)):
            line.append(input_array[j][i])
        flatten.append(line)
    return flatten


def get_max_length(input_board):
    res_arr = []
    for array in flatten_2d_array(input_board):
        res_arr.append(check_continuous_char(array))
    return max(res_arr)


input = sys.stdin.readline
count = int(input())
board = [list(input().rstrip()) for i in range(count)]
result = []

for i in range(count):
    for j in range(count - 1):
        board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        result.append(get_max_length(board))
        board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

for i in range(count):
    for j in range(count - 1):
        board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]
        result.append(get_max_length(board))
        board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]

print(max(result))