from collections import deque


def get_structure(input_r, input_c, input_m):
    global res_s, res_d
    water = []
    for i in range(input_r):
        for j in range(input_c):
            if input_m[i][j] == 'S':
                res_s = (i, j)
            elif input_m[i][j] == '*':
                water.append((i, j))
            elif input_m[i][j] == 'D':
                res_d = (i, j)
    return res_s, res_d, water


r, c = map(int, input().split())
m = [list(input()) for _ in range(r)]
s, d, water = get_structure(r, c, m)
s_i, s_j = s
d_i, d_j = d

m[s_i][s_j] = 0
deque = deque(water)
deque.append((s_i, s_j))


def set_water(t_i, t_j):
    # 위쪽
    if 0 <= t_i - 1 < r and m[t_i-1][t_j] == '.':
        m[t_i-1][t_j] = '*'
        deque.append((t_i-1, t_j))
    # 아래
    if 0 <= t_i + 1 < r and m[t_i+1][t_j] == '.':
        m[t_i+1][t_j] = '*'
        deque.append((t_i+1, t_j))
    # 왼쪽
    if 0 <= t_j - 1 < c and m[t_i][t_j-1] == '.':
        m[t_i][t_j-1] = '*'
        deque.append((t_i, t_j-1))
    # 오른쪽
    if 0 <= t_j + 1 < c and m[t_i][t_j+1] == '.':
        m[t_i][t_j+1] = '*'
        deque.append((t_i, t_j+1))


def set_field(curr_count, t_i, t_j):
    # 위쪽
    if 0 <= t_i - 1 < r and m[t_i - 1][t_j] == '.':
        m[t_i-1][t_j] = curr_count + 1
        deque.append((t_i-1, t_j))
    # 아래
    if 0 <= t_i + 1 < r and m[t_i + 1][t_j] == '.':
        m[t_i + 1][t_j] = curr_count + 1
        deque.append((t_i+1, t_j))
    # 왼쪽
    if 0 <= t_j - 1 < c and m[t_i][t_j - 1] == '.':
        m[t_i][t_j-1] = curr_count + 1
        deque.append((t_i, t_j-1))
    # 오른쪽
    if 0 <= t_j + 1 < c and m[t_i][t_j + 1] == '.':
        m[t_i][t_j+1] = curr_count + 1
        deque.append((t_i, t_j+1))


def get_result(t_i, t_j):
    res = []
    # 위쪽
    if 0 <= t_i - 1 < r and m[t_i - 1][t_j] != '.' and m[t_i - 1][t_j] != '*' and m[t_i - 1][t_j] != 'X':
        res.append(int(m[t_i - 1][t_j]))
    # 아래
    if 0 <= t_i + 1 < r and m[t_i + 1][t_j] != '.' and m[t_i + 1][t_j] != '*' and m[t_i + 1][t_j] != 'X':
        res.append(int(m[t_i + 1][t_j]))
    # 왼쪽
    if 0 <= t_j - 1 < c and m[t_i][t_j - 1] != '.' and m[t_i][t_j - 1] != '*' and m[t_i][t_j - 1] != 'X':
        res.append(int(m[t_i][t_j - 1]))
    # 오른쪽
    if 0 <= t_j + 1 < c and m[t_i][t_j + 1] != '.' and m[t_i][t_j + 1] != '*' and m[t_i][t_j + 1] != 'X':
        res.append(int(m[t_i][t_j + 1]))
    return res


while deque:
    i, j = deque.popleft()
    if m[i][j] == 'D':
        break
    elif m[i][j] == '*':
        set_water(i, j)
    else:
        set_field(int(m[i][j]), i, j)

result = get_result(d_i, d_j)
if len(result) == 0:
    print('KAKTUS')
else:
    print(min(result) + 1)
