from collections import deque

def get_circular(deque, index):
    return deque[index % len(deque)]


def get_count(deque, start, length):
    curr = deque[start]
    res = 1
    for i in range(start, start+length+1):
        value = get_circular(deque, i)
        if curr == value:
            res += 1
        curr = value
    return res


p = input()
s = int(input())

play_list = list(map(int, p.split(' ')))

if len(play_list) <= s:
    print(len(play_list))
    exit()

play_time_interval = deque([0 for _ in range(sum(play_list))])

index = 0
for i, play_min in enumerate(play_list):
    for j in range(play_min):
        play_time_interval[index] = i
        index += 1


res = 1000000000
for i in range(len(play_time_interval)):
    res = min(get_count(play_time_interval, i, s), res)

print(res)









