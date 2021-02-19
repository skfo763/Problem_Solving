state_graph = [
    [1, 2],
    [-1, 3],
    [4, -1],
    [1, 2],
    [5, -1],
    [5, 6],
    [1, 7],
    [8, 7],
    [5, 0]
]

count = int(input())
for _ in range(count):
    test = list(map(int, input()))
    curr_state = 0
    for i in range(len(test)):
        flag = 0 if test[i] == 0 else 1
        t = state_graph[curr_state][flag]
        if t >= 0:
            curr_state = t
        else:
            curr_state = -1
            break

    if curr_state == 0 or curr_state == 3 or curr_state == 6 or curr_state == 7:
        print("YES")
    else:
        print("NO")