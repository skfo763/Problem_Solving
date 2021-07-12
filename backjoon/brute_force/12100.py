n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def print_board(input_board):
    for line in input_board:
        print(line)


def get_max_block(input_board):
    return max(input_board)


def move_top(input_n, input_board):
    for i in range(input_n-1, 0, -1):
        for j in range(input_n):
            if input_board[i][j] == input_board[i-1][j]:
                input_board[i][j] = 0
                input_board[i-1][j] *= 2
            elif input_board[i-1][j] == 0:
                temp = input_board[i][j]
                input_board[i][j] = 0
                input_board[i-1][j] = temp
    return input_board


def move_bottom(input_n, input_board):
    for i in range(input_n-1):
        for j in range(input_n):
            if input_board[i][j] == input_board[i+1][j]:
                input_board[i][j] = 0
                input_board[i+1][j] *= 2
            elif input_board[i+1][j] == 0:
                temp = input_board[i][j]
                input_board[i][j] = 0
                input_board[i+1][j] = temp
    return input_board


def move_left(input_n, input_board):
    for i in range(input_n-1, 0, -1):
        for j in range(input_n):
            if input_board[j][i] == input_board[j][i-1]:
                input_board[j][i] = 0
                input_board[j][i-1] *= 2
            elif input_board[j][i-1] == 0:
                temp = input_board[i][j]
                input_board[j][i] = 0
                input_board[j][i-1] = temp
    return input_board


def move_right(input_n, input_board):
    for i in range(input_n-1):
        for j in range(input_n):
            if input_board[j][i] == input_board[j][i+1]:
                input_board[j][i] = 0
                input_board[j][i+1] *= 2
            elif input_board[j][i+1] == 0:
                temp = input_board[i][j]
                input_board[i][j] = 0
                input_board[j][j+1] = temp
    return input_board


def func(input_board, k):
    if k == 0:
        return [input_board]
    else:
        prev = func(input_board, k-1)
        res = []
        for prev_board in prev:
            res.append(move_top(len(prev_board), prev_board))
            res.append(move_bottom(len(prev_board), prev_board))
            res.append(move_left(len(prev_board), prev_board))
            res.append(move_right(len(prev_board), prev_board))
        return res


test_board = [[1]*4 for _ in range(4)]
result = move_top(len(test_board), test_board)
print_board(result)

# for board in test_result:
#    print_board(board)





