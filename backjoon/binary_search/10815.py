number_card_count = int(input())
number_card_list = list(map(int, input().split()))
target_number_count = int(input())
target_number_list = list(map(int, input().split()))

sorted_list = sorted(number_card_list)

for number in target_number_list:
    low = 0
    high = len(sorted_list) - 1
    is_exist = False

    while low <= high:
        mid = (low + high) // 2
        mid_value = sorted_list[mid]
        if number > mid_value:
            low = mid + 1
        elif number < mid_value:
            high = mid - 1
        else:
            is_exist = True
            break

    if is_exist:
        print("1", end=" ")
    else:
        print("0", end=" ")
