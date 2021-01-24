import sys
input = sys.stdin.readline


def get_good_section_count(input_set, input_num):
    if input_num in input_set:
        return 0
    input_set.append(input_num)
    input_set = sorted(input_set)
    index = input_set.index(input_num)
    start = index - 1
    end = index + 1
    if index == 0:
        return (input_set[1] - input_set[0]) * input_set[0] - 1
    else:
        return (input_set[index] - input_set[start]) * (input_set[end] - input_set[index]) - 1


set_count = int(input().rstrip())
given_set = map(int, input().rstrip().split())
number = int(input().rstrip())

print(get_good_section_count(list(given_set), number))