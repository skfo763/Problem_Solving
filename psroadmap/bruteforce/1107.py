import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def f(input_list, count):
    if count == 1:
        return input_list
    else:
        temp_list = []
        l = f(input_list, count - 1)
        for i in input_list:
            for j in l:
                temp_list.append(j + i)
        return temp_list


target_channel = int(input().rstrip())
disabled_key_count = int(input().rstrip())
if disabled_key_count == 0:
    disabled_key = set()
else:
    disabled_key = set(map(int, input().rstrip().split()))

enabled_key = list(set([i for i in range(10)]) - disabled_key)

if len(enabled_key) == 0:
    print(abs(100 - target_channel))
else:
    enabled_key_str = list(map(str, enabled_key))

    available_channel = []
    for i in range(1, 7):
        for j in list(map(int, f(enabled_key_str, i))):
            available_channel.append(j)

    available_channel = list(set(available_channel))
    distance = list(map(lambda x: abs(target_channel - x) + len(str(x)), available_channel))
    min_value = min(distance)
    just_move_result = abs(100 - target_channel)
    print(min(min_value, just_move_result))

