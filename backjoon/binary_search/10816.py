from bisect import bisect_left, bisect_right

n = int(input())
card_list = list(map(int, input().split()))
m = int(input())
target_list = list(map(int, input().split()))
card_list = sorted(card_list)

for i in target_list:
    left = bisect_left(card_list, i)
    right = bisect_right(card_list, i)
    print(right - left, end=" ")

