import sys
input = sys.stdin.readline


def get_minimum_revise(input_chess_board):
    seq_white = ["W", "B", "W", "B", "W", "B", "W", "B", "B", "W", "B", "W", "B", "W", "B", "W"] * 4
    seq_black = ["B", "W", "B", "W", "B", "W", "B", "W", "W", "B", "W", "B", "W", "B", "W", "B"] * 4
    res_white = 0
    res_black = 0
    for i in range(64):
        if input_chess_board[i] == seq_white[i]:
            res_white += 1
        if input_chess_board[i] == seq_black[i]:
            res_black += 1
    return min(res_white, res_black)


def get_fit_chess_board(input_chess_board, x_start, y_start):
    result_board = []
    for i in range(y_start,  y_start+8):
        for j in range(x_start, x_start+8):
            result_board.append(input_chess_board[i][j])
    return result_board


n, m = map(int, input().rstrip().split())
chess_board = []
result = []

for i in range(n):
    chess_board.append(list(input().rstrip()))

for i in range(0, n - 7):
    for j in range(0, m - 7):
        fit_chess_board = get_fit_chess_board(chess_board, j, i)
        result.append(get_minimum_revise(fit_chess_board))

print(min(result))