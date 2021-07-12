from collections import deque


def get_flatten_str(count, base_str):
    res = ""
    for i in range(int(count)):
        res += base_str
    return res


def get_comp_array(compressed):
    num_arr = []
    res = []
    current_number = True

    if compressed[0].isdigit():
        num_arr.append(compressed[0])
    else:
        res.append(compressed[0])
        current_number = False

    for i in range(1, len(compressed)):
        if compressed[i].isdigit():
            num_arr.append(compressed[i])
            current_number = True
        else:
            if current_number:
                res.append(''.join(num_arr))
                num_arr.clear()
                res.append(compressed[i])
            else:
                res.append(compressed[i])
            current_number = False
    return res


def solution(compressed):
    stack = deque([])
    comp_array = get_comp_array(compressed)

    for c in comp_array:
        if c == ')':
            cumm_str = ""
            while True:
                pop_str = stack.pop()
                if pop_str == '(':
                    break
                else:
                    cumm_str += pop_str
            count = stack.pop()
            stack.append(get_flatten_str(count, cumm_str))
        else:
            stack.append(c)

    res_str = ""
    while stack:
        pop_str = stack.pop()
        if pop_str == '(':
            break
        else:
            res_str += pop_str

    print(res_str[::-1])

solution("2(2(hi)2(co))x2(bo)")